from django.db import models
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя товара')
    price = models.FloatField(verbose_name='Цена товара', default=0.0)
    description = models.TextField(verbose_name='Описание товара')
    image = models.ImageField(verbose_name='Картинка товара')
    slug = models.SlugField()
    publish = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('catalog:detail',
                       kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-publish']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория мебели')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category_products', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-name']
