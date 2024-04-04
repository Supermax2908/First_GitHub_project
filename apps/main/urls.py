from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.greeting, name='greeting'),
    path('site/', views.about_site, name='about_site')
]