from django.urls import path
from .views import question_list, create_question, create_answer

urlpatterns = [
    path('', question_list, name='question_list'),
    path('create_question', create_question, name='create_question'),
    path('create_answer', create_answer, name='create_answer')
]
