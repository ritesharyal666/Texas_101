from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from blog.forms import CommentForm, PostForm
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
        'post':post,
        'comment_form': CommentForm(),
    }
    return render(request,'blog/post_detail.html',context=context)



def user_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'blog/login.html', context=context)

def user_logout_view(request):
    logout(request)
    return redirect('home')


def post_create_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', context={'form': form})

def post_edit_view(request, slug):
    if not request.user.is_authenticated:
        return redirect('login')
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.category_id = request.POST.get('category')
        if 'featured_image' in request.FILES:
            post.featured_image = request.FILES['featured_image']
        post.save()
        return redirect('post_detail', slug=post.slug)
    context = {
        'post': post
    }
    return render(request, 'blog/post_edit.html', context=context)

def post_delete_view(request, slug):
    if not request.user.is_authenticated:
        return redirect('login')
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {
        'post': post
    }
    return render(request, 'blog/post_confirm_delete.html', context=context)

def add_comment_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    return redirect('post_detail', slug=post.slug)

