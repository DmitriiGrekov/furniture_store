from django.db import models
from django.urls import reverse


class RubricCompany(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название пункта меню')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Название пункта меню'
        verbose_name_plural = 'Названия пункта меню'


class ReviewsCompany(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    company = models.CharField(max_length=100, verbose_name='Компания',
                               blank=True,
                               null=True)
    position = models.CharField(max_length=120, verbose_name='Должность',
                                blank=True,
                                null=True)
    content = models.TextField(verbose_name='Текст отзыва')
    publish = models.DateField(auto_now_add=True)
    img = models.ImageField(verbose_name='Аватарка', blank=True, null=True)
    files = models.ManyToManyField('ReviewsFiles',
                                   related_name='reviews_files',
                                   blank=True,
                                   null=True)
    slug = models.SlugField(verbose_name='slug')

    def get_absolute_url(self):
        return reverse('company:detail_review', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ReviewsFiles(models.Model):
    files = models.FileField(verbose_name='Файлы к отыву')

    def __str__(self):
        return self.files.name

    class Meta:
        verbose_name = 'Файл к отзыву'
        verbose_name_plural = 'Файлы к отзыву'
