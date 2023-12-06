from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug_id>/', views.get_posts, name='group'),
    path('post/<int:post_id>/', views.get_one_post, name='post')
]
