from django.contrib.auth import get_user_model, login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import RegisterForm


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
    success_message = "Your profile was created successfully"


def login_without_credentials(request):
    User = get_user_model()
    user = User.objects.get(id=2)

    if user is not None:
        login(request, user)
        return redirect('courses:dashboard')
