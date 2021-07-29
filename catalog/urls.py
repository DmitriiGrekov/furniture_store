from django.urls import path
from .views import CatalogListView, CatalogCategoryView, CatalogDetailView

app_name = 'catalog'
urlpatterns = [
    path('', CatalogListView.as_view(), name='list'),
    path('category/<slug:slug>/', CatalogCategoryView.as_view(),
         name='category_products'),
    path('detail/<slug:slug>/', CatalogDetailView.as_view(), name='detail'),

]
