from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home_view(request):
    posts = Post.objects.all()[:4]
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html',context=context)

def about_view(request):
    return render(request, 'blog/about.html')

def contact_view(request):
    return render(request, 'blog/contact.html')

def search_view(request):
    query = request.GET.get('search_query',"")
    results=[]
    results = Post.objects.filter(title__icontains=query)
    context={
        'query':query,
        'results':results
    }
    return render(request,'blog/search.html',context=context)

def post_list_view(request):
    posts = Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'blog/post_list.html',context=context)

def post_detail_view(request,slug):
    post = Post.objects.get(slug=slug)
    context={
        'post':post
    }
    return render(request,'blog/post_detail.html',context=context)


