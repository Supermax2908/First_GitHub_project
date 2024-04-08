from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    all_posts = Post.objects.all()
    count_posts = all_posts.count()
    count_comments = Comment.objects.all().count()
    context = {
        'all_posts': all_posts,
        'created_form': PostForm(),
        'count_posts': count_posts,
        'count_comments': count_comments
    }
    return render(request, 'article/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    count_comments = Comment.objects.all().count()
    context = {
        'post': post,
        'count_comments': count_comments
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
def delete_view(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id, author=request.user)
        post.delete()
    return redirect('article:index')

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
    

@login_required
def comment_view(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                post = post,
                author = request.user,
                content = form.cleaned_data['content']
            )
    return redirect('article:detail', post_id=post.id)

@login_required
def like_comment_view(request, comment_id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment, pk=comment_id)
    if request.user in comment.like.all():
        comment.like.remove(request.user)
        user_like = False
    else:
        comment.like.add(request.user)
        user_like = True
        return JsonResponse({'like_count': comment.like.count(), 'user_like': user_like})
    
    
@login_required
def dislike_comment_view(request, comment_id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment, pk=comment_id)
    if request.user in comment.dislike.all():
        comment.dislike.remove(request.user)
        user_dislike = False
    else:
        comment.dislike.add(request.user)
        user_dislike = True
        return JsonResponse({'dislike_count': comment.dislike.count(), 'user_dislike': user_dislike})
