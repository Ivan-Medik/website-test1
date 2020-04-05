from django.shortcuts import render
from .models import Post

from django.db.models import Q

def posts_list(request):
    search_querry = request.GET.get('search','')

    if search_querry:
        posts = Post.objects.filter(Q(title__icontains=search_querry) | Q(body__icontains=search_querry))
    else:
        posts = Post.objects.all()

    return render(request, "blog/index.html", context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})
