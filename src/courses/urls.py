from django.urls import path

from . import views


app_name = 'courses'
urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('teacher/', views.TeacherDashboard.as_view(), name='teacher_dashboard'),
    path('student/', views.StudentDashboard.as_view(), name='student_dashboard'),
]
