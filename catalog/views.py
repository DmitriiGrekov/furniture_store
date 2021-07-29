from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Products, Category


class CatalogListView(ListView):
    template_name = 'catalog/list.html'
    context_object_name = 'products'
    queryset = Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_products'] = Category.objects.all()
        return context


class CatalogCategoryView(ListView):
    template_name = 'catalog/catalog_rubric.html'
    model = Products
    context_object_name = 'catalog_of_rubrics'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Products.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_products'] = Category.objects.all()
        context['current_category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class CatalogDetailView(DetailView):
    template_name = 'catalog/detail.html'
    model = Products
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_products'] = Category.objects.all()
        return context
