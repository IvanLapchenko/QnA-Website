from django.urls import path
from .views import render_main_page, create_question, create_answer, search, render_categories_page, \
    render_question_page, edit_question, edit_answer

urlpatterns = [
    path('', render_main_page, name='question_list'),
    path('create_question', create_question, name='create_question'),
    path('create_answer', create_answer, name='create_answer'),
    path('search', search, name='search'),
    path('categories', render_categories_page, name='render_categories_page'),
    path('question', render_question_page, name='render_question_page'),
    path('question/edit/<int:question_id>/', edit_question, name='edit_question'),
    path('answer/edit/<int:answer_id>/', edit_answer, name='edit_answer')
]
