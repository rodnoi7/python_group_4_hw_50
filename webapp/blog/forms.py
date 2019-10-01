from django import forms
from blog.models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['parrent_comment', 'text', 'author']

class CommentAnswerForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ['author', 'parrent_comment', 'article']