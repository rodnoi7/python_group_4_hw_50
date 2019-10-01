from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from blog.models import Article
from blog.forms import ArticleForm
from django.urls import reverse, reverse_lazy

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_view.html'

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_update.html'
    success_url = reverse_lazy('index')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('index')

class ArticleCreateView(CreateView):
   model = Article
   form_class = ArticleForm
   template_name = 'add_article.html'
   success_url = reverse_lazy('index')