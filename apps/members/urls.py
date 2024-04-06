from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('singup/', views.singup_view, name='singup')
]