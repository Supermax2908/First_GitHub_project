from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from apps.article.models import Post
from apps.article.forms import PostForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:about_site')
    form = AuthenticationForm(request, request.POST)
    return render(request, 'members/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('main:about_site')


def singup_view(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:about_site')
    return render(request, 'members/singup.html', {'form': form})


@login_required
def profile_view(request):
    posts = Post.objects.filter()
    created_form = PostForm()
    context = {
        'posts': posts,
        'created_form': created_form
    }
    return render(request, 'members/profile.html', context)