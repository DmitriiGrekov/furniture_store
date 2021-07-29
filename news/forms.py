from django import forms
from .models import NewsModel


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsModel
        fields = ('title', 'author', 'description',)
