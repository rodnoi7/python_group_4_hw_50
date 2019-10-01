"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView, CommentCreateView, CommentDeleteView, AnswerCommentCreateView, change_comment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='view'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='del_article'),
    path('article/create', ArticleCreateView.as_view(), name='article_create'),

    path('article/<int:pk>/add_comment', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='del_comment'),
    path('article/<int:pk>/comment/<int:comment_pk>/create_answer', AnswerCommentCreateView.as_view(), name='add_answer_comment'),
    path('article/<int:article_pk>/comment/<int:comment_pk>/update', change_comment, name='change'),
]
urlpatterns += staticfiles_urlpatterns()