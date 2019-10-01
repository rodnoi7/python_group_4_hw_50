from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    author = models.CharField(max_length=40, null=False, blank=False, default='Аноним', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return '%s (%s) - %s' % (self.title, self.created_at, self.author)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    parrent_comment = models.ForeignKey('Comment', null=True, blank=True, related_name='parr_coment', on_delete=models.CASCADE, verbose_name='Ответ на:')

    def __str__(self):
        return self.text[:20]