from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', register, name='register'),
]