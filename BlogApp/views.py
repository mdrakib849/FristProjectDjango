from django.shortcuts import render
from .models import Post


def homepage(request):
    Posts = Post.objects.all()
    return render(request, 'home/homepage.html', {"Posts": Posts})


def about(request):
    return render(request, 'home/about.html', {"title": "About page"})
