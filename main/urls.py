from django.urls import path
from .views import MainTemplateView


app_name = 'main'
urlpatterns = [
    path('', MainTemplateView.as_view(), name='index'),
]
