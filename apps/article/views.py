from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    all_posts = Post.objects.all()
    count_posts = all_posts.count()
    context = {
        'all_posts': all_posts,
        'created_form': PostForm(),
        'count_posts': count_posts
    }
    return render(request, 'article/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'article/detail.html', context)


def create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('article:detail', post_id=post.id)
        
@login_required
def like_view(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        if request.user in post.like.all():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)
        return JsonResponse({'like_count': post.like.count()})
        
        
@login_required
def dislike_view(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        if request.user in post.dislike.all():
            post.dislike.remove(request.user)
        else:
            post.dislike.add(request.user)
        return JsonResponse({'dislike_count': post.dislike.count()})
