from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post, Group


def index(request: HttpRequest):
    posts = Post.show_group.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context=context)


def get_posts(request, slug_id):
    group = get_object_or_404(Group, slug=slug_id)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    return render(request, 'posts/group_list.html', context={'title': 'Записи сообществ', 'posts': posts})


def get_one_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'title': f'Пост {post.pk}',
        'post': post
    }
    return render(request, 'posts/post.html', context=context)





