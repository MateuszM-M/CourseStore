from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'courses/dashboard.html'


class TeacherDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'courses/teacher/teacher_dashboard.html'
    
    
class StudentDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'courses/student/student_dashboard.html'