from django.urls import path
from .views import render_main_page, create_question, create_answer

urlpatterns = [
    path('', render_main_page, name='question_list'),
    path('create_question', create_question, name='create_question'),
    path('create_answer', create_answer, name='create_answer')
]
