from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post',
        'content': 'First Post content',
        'date_posted': 'April, 04, 2023'
    },
    {
        'author': 'Parkhi Goyal',
        'title': 'Blog Post 2',
        'content': 'First Post content',
        'date_posted': 'April, 04, 2023'
    }
]


def home(request):
    # dictionary named context
    context = {
        'posts' :posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
