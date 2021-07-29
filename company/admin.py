from django.contrib import admin
from .models import RubricCompany, ReviewsCompany, ReviewsFiles


class RubricAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'publish',)
    list_display_links = ('name', 'company',)
    search_fields = ('name', 'company')
    prepopulated_fields = {'slug': ('name', 'company',)}


admin.site.register(RubricCompany, RubricAdmin)
admin.site.register(ReviewsCompany, ReviewsAdmin)
admin.site.register(ReviewsFiles)
