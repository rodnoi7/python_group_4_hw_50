from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from blog.models import Article, Comment
from blog.forms import ArticleForm, CommentForm, CommentAnswerForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

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

class CommentCreateView(CreateView):
   model = Comment
   form_class = CommentForm
   template_name = 'add_comment.html'
   success_url = reverse_lazy('index')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['article_pk'] = self.kwargs.get('articelpk')
       return context

   def form_valid(self, form):
       form.instance.article = Article.objects.get(pk=self.kwargs.get('articlepk'))
       return super().form_valid(form)

   def get_success_url(self):
       return reverse('view', kwargs={'pk': self.object.article.pk})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('index')

class AnswerCommentCreateView(CreateView):
    model = Comment
    form_class = CommentAnswerForm
    template_name = 'add_answer_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_pk']=self.kwargs.get('pk')
        context['parrent_comment']=self.kwargs.get('comment_pk')
        return context

    def form_valid(self, form):
        form.instance.article = Article.objects.get(pk=self.kwargs.get('pk'))
        form.instance.parrent_comment = Comment.objects.get(pk=self.kwargs.get('comment_pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.article.pk})

def change_comment(request, article_pk, comment_pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=comment_pk)
        context = {
            'comment': comment,
        }
        return render(request, 'update_comment.html', context)
    elif request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        article = Article.objects.get(pk=article_pk)
        comment.text = request.POST.get('text')
        comment.save()
        comment = Comment.objects.all()
        context = {
            'comment': comment
        }
        return redirect('view', article_pk)