from django.contrib import admin
from .models import NewsModel


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish',)
    list_display_links = ('title', 'author')
    search_fields = ('title', 'author',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(NewsModel, NewsAdmin)
