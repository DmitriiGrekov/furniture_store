from rest_framework import serializers
from .models import NewsModel


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsModel
        fields = ('title', 'author', 'description', 'publish', 'slug')
