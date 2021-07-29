from django.views.generic.base import TemplateView
from news.models import NewsModel


class MainTemplateView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NewsModel.objects.all().order_by('-publish')[:6]
        return context
