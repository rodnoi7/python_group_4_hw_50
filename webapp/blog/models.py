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

