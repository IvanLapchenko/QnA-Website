from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
from .controllers import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page


def render_main_page(request):
    questions = Question.objects.all().prefetch_related('answer_set')
    question_form = QuestionForm()
    answer_form = AnswerForm()
    return render(request, 'main.html', {'questions': questions,
                                         'question_form': question_form,
                                         'answer_form': answer_form})


@cache_page(60 * 60)
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.publish()
            messages.success(request, 'Your question has been posted successfully!')
        else:
            messages.error(request, 'There was an error posting your question. Please try again.')
    return redirect('/')


@cache_page(60 * 60)
def create_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            question_pk = request.POST.get('question_pk')
            print(question_pk)
            question = Question.objects.get(pk=question_pk)
            answer.question = question
            answer.author = request.user
            answer.publish()
            messages.success(request, 'Your answer has been posted successfully!')
        else:
            messages.error(request, 'There was an error posting your answer. Please try again.')
    return redirect('/')


def search(request):
    query = request.GET.get('q')
    questions = Question.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    context = {
        'questions': questions,
        'title': f'Search result for {query}',
    }
    return render(request, 'main.html', context)


@cache_page(60 * 60)
def render_categories_page(request):
    return render(request, 'categories.html', {'categories': get_all_categories()})


def render_question_page(request):
    question_id = request.GET.get('pk')
    answer_form = AnswerForm()
    return render(request, 'question.html', {'question': get_question_by_id(question_id),
                                             'answers': get_answers_for_question(question_id),
                                             'answer_form': answer_form})


def render_user_page(request):
    questions = get_questions_for_user(request.user)
    return render(request, 'main.html', {'questions': questions})


@login_required
def edit_model(request, model, record_id):
    object_class = Question if model == "Question" else Answer
    form_class = QuestionForm if model == "Question" else AnswerForm

    record = get_object_or_404(object_class, pk=record_id)
    if request.method == 'POST':
        form = form_class(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = form_class(instance=record)
        return render(request, 'edit_record.html', {'form': form, 'model': model})


def render_ask_question_page(request):
    question_form = QuestionForm()
    return render(request, 'ask_question.html', {'question_form': question_form})


@login_required
def delete_model(request, model, record_id):
    if model == 'Question':
        return delete_record(request, Question, record_id)
    elif model == 'Answer':
        return delete_record(request, Answer, record_id)


def vote(request, model, action, record_id):
    model_mapping = {
        'question': Question,
        'answer': Answer
    }
    model_class = model_mapping.get(model)

    record = get_object_or_404(model_class, pk=record_id)

    if isinstance(record, Answer):
        redirect_id = record.question.id
    else:
        redirect_id = record_id

    try:
        if action == 'upvote':
            record.upvote(request.user.id)
        elif action == 'downvote':
            record.downvote(request.user.id)
        resp_data = 'ok'
    except Exception as e:
        print(e)
        resp_data = str(e)

    return redirect(f'/question?pk={redirect_id}')