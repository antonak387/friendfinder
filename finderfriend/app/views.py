from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def profile(request):
    return render(request, 'app/profile.html')


def likes(request):
    return render(request, 'app/likes.html')


def matches(request):
    return render(request, 'app/likes.html')
