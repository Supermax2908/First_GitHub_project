from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
        path('', views.index, name='index'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    
    path('create/', views.create_view, name='create'),
    path('delete/<int:post_id>/', views.delete_view, name='delete'),
    
    path('like/<int:post_id>/', views.like_view, name='like'),
    path('dislike/<int:post_id>/', views.dislike_view, name='dislike'),
    
    path('post/<int:post_id>/comment/', views.comment_view, name='comment'),
    path('like_comment/<int:comment_id>/', views.like_comment_view, name="like_comment"),
    path('dislike_comment/<int:comment_id>/', views.dislike_comment_view, name="dislike_comment")
]