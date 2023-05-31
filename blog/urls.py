from django.urls import path
from .views import render_main_page, create_question, create_answer, search, render_categories_page, \
    render_question_page, edit_question, edit_answer, render_ask_question_page, delete_question, \
    delete_answer

urlpatterns = [
    path('', render_main_page, name='main_page'),
    path('create_question', create_question, name='create_question'),
    path('create_answer', create_answer, name='create_answer'),
    path('search', search, name='search'),
    path('categories', render_categories_page, name='render_categories_page'),
    path('question', render_question_page, name='question'),
    path('Question/edit/<int:question_id>/', edit_question, name='edit_question'),
    path('Answer/edit/<int:answer_id>/', edit_answer, name='edit_answer'),
    path('Question/delete/<int:question_id>/', delete_question, name='delete_question'),
    path('Answer/delete/<int:answer_id>/', delete_answer, name='delete_answer'),
    path('ask_question', render_ask_question_page, name='ask_question'),
]
