from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from .models import Course


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'courses/dashboard.html'


class TeacherDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'courses/teacher/teacher_dashboard.html'
    

class CreateCourse(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['subject', 'title', 'overview']
    template_name = 'courses/teacher/create_course.html'
      
    
class StudentDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'courses/student/student_dashboard.html'