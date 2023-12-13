from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post, Group
import datetime


def index(request: HttpRequest):
    posts = Post.show_group.all().select_related('author').select_related('group')
    d = Post.objects.filter(text__contains='утро').filter(author_id=2).filter(pub_date__range=(datetime.date(1854, 7, 7), datetime.date(1854, 7, 21)))
    context = {
        'posts': posts,
        'd': d
    }
    return render(request, 'posts/index.html', context=context)


def get_posts(request, slug_id):
    group = get_object_or_404(Group, slug=slug_id)
    posts = Post.objects.filter(group=group).select_related('author').order_by('-pub_date')
    return render(request, 'posts/group_list.html', context={'title': 'Записи сообществ', 'posts': posts, 'group': group})


def get_one_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'title': f'Пост {post.pk}',
        'post': post
    }
    return render(request, 'posts/post.html', context=context)





