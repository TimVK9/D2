from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import PostForm
from .models import Post
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    context_object_name = 'posts'
    template_name = 'news/default.html'
    paginate_by = 10


class PostSearch(PostList):
    template_name = 'news/search.html'

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter()
        }


class DetailPost(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/news.html'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/postcreate.html'
    success_url = '/news/search'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NEWS'
        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_article',)
    form_class = PostForm
    model = Post
    template_name = 'news/articlecreate.html'
    success_url = '/news/search'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'ARTICLE'
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/postcreate.html'
    success_url = '/news/search'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_article',)
    model = Post
    template_name = 'news/delete.html'
    success_url = '/news/search'


def search_post(request):
    form = PostFilter()

    return render(request, 'search.html', {'form': form})
