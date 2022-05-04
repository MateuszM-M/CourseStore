from django.shortcuts import render


def handle_404(request, exception):
    return render(request, 'errors/404.html')


def handle_500(request):
    return render(request, 'errors/500.html')


def handle_403(request, exception):
    return render(request, 'errors/403.html')


def handle_400(request, exception):
    return render(request, 'errors/400.html')

