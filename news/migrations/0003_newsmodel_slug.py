# Generated by Django 3.2.5 on 2021-07-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210719_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='slug',
            field=models.SlugField(default=1, verbose_name='Человеко-понятная ссылка'),
            preserve_default=False,
        ),
    ]
