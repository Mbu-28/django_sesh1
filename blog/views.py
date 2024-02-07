from django.shortcuts import render
from .models import Post

def home(request):
    # Used a dictionary 'context' to get data from dictionary 'posts'
    context = {
        'posts': Post.objects.all()

    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})

