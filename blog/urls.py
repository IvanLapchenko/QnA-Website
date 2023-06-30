from django.urls import path
from .views import render_main_page, create_question, create_answer, search, render_categories_page, \
    render_question_page, edit_model, render_ask_question_page, delete_model, render_user_page, vote

urlpatterns = [
    path('', render_main_page, name='main_page'),
    path('create_question', create_question, name='create_question'),
    path('create_answer', create_answer, name='create_answer'),
    path('search', search, name='search'),
    path('categories', render_categories_page, name='render_categories_page'),
    path('question', render_question_page, name='question'),
    path('ask_question', render_ask_question_page, name='ask_question'),
    path('user_page', render_user_page, name='user_page'),
    path('<model>/edit/<int:record_id>/', edit_model, name='edit_record'),
    path('<model>/delete/<int:question_id>/', delete_model, name='delete_model'),
    path('<model>/<action>/<int:record_id>/', vote, name='vote'),
]
