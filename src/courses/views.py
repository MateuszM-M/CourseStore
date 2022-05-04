from django.shortcuts import render, redirect
from django.views import View


class Dashboard(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        return render(request, 'courses/dashboard.html')

