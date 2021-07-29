from django.db import models


class UsefullInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок блока')
    content = models.CharField(max_length=100, verbose_name='Содержание блока')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Содержимое блока "Полезная информация"'
        verbose_name_plural = 'Содержимое блока "Полезная информация"'
