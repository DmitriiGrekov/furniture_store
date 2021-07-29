from django import forms
from .models import ReviewsCompany


class ReviewFormAdd(forms.ModelForm):
    files = forms.FileField(widget=forms.widgets.ClearableFileInput(attrs={'multiple': True}))
    img = forms.ImageField()

    class Meta:
        model = ReviewsCompany
        fields = ('name', 'position', 'company', 'content', 'img', 'files',)
