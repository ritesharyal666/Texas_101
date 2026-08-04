from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home_view(request):
    posts = Post.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html',context=context)

def about_view(request):
    return render(request, 'blog/about.html')

def contact_view(request):
    return render(request, 'blog/contact.html')