from django.db import models
from django.urls import reverse


class NewsModel(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок новости')
    author = models.CharField(max_length=300,
                              verbose_name='Автор или авторы',
                              blank=True,
                              null=True)
    description = models.TextField(verbose_name='Описание объявления')
    publish = models.DateField(auto_now_add=True,
                               verbose_name='Дата публикации')
    slug = models.SlugField(verbose_name='Человеко-понятная ссылка')

    def get_absolute_url(self):
        return reverse('news:news_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
