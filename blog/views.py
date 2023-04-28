from django.shortcuts import render, redirect
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


def question_list(request):
    questions = Question.objects.all().prefetch_related('answers')
    context = {'questions': questions}
    return render(request, 'main.html', context)


def create_question(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.publish()
            return redirect('question_detail', pk=question.pk)
    return render(request, 'main.html', {'form': form})


def create_answer(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.publish()
            return redirect('question_detail', pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'main.html', {'form': form, 'question': question})

