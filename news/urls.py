from django.urls import path
from .views import NewsListView, NewsDetailView
from .views import NewsEditView


# api
# from .views import api_news, api_news_detail
from .views import ApiNewsAllAndCreate, ApiNewsMethods

app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name='list'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('create/news/', NewsEditView.as_view(), name='create'),
    path('api/all', ApiNewsAllAndCreate.as_view(), name='api'),
    path('api/<slug:slug>', ApiNewsMethods.as_view()),
]
