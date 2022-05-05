from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', 
        auth_views.LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='registration/login.html'),
        name='login'),
    path('logout/', 
        auth_views.LogoutView.as_view(
            template_name='registration/logout.html'), 
        name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register')
]
