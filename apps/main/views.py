from django.shortcuts import render

# Create your views here.

def greeting(request):
    return render(request, 'main/greeting.html')

def about_site(request):
    return render(request, 'main/about_site.html')