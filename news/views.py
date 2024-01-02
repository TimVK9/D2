from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/default.html'


class DetailPost(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/news.html'
