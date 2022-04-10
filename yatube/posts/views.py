from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'text': "Последние обновления на сайте",
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts, 'group': group
    }
    return render(request, 'posts/group_list.html', context)


def group_list(request):
    group_list = 'posts/group_list.html'
    return render(request, group_list)
