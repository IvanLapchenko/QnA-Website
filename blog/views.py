from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


def render_main_page(request):
    questions = Question.objects.all().prefetch_related('answer_set')
    question_form = QuestionForm()
    answer_form = AnswerForm()
    return render(request, 'main.html', {'questions': questions,
                                         'question_form': question_form,
                                         'answer_form': answer_form})


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


def create_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            question_pk = request.POST.get('question_pk')
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
        'query': query,
    }
    return render(request, 'search.html', context)