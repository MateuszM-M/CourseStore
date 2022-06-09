from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, TemplateView, ListView
from .forms import AddCourseForm

from .models import Course, Module


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'courses/dashboard.html'


class TeacherDashboard(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/teacher/teacher_dashboard.html'
    
    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
    

class CreateCourse(LoginRequiredMixin, CreateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'courses/teacher/create_course.html'
    success_url = '/teacher/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
                
class CreateModule(LoginRequiredMixin, CreateView):
    model = Module
    template_name = 'courses/teacher/create_module.html'
    
class StudentDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'courses/student/student_dashboard.html'
