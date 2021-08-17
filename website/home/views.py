from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *
# Create your views here.


class ArticleListView(ListView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    extra_context = {'page_title': 'Create'}


class ArticleDetailView(DetailView):
    model = Article


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    extra_context = {'page_title': 'update'}


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('home')
