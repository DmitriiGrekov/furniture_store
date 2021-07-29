from django.contrib import admin
from .models import Products, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'publish',)
    list_display_links = ('name', 'price', )
    search_fields = ('name', 'price', 'category')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
