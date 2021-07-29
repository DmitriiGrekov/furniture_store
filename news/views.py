from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.template.defaultfilters import slugify
from unidecode import unidecode
from .models import NewsModel
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin

# api
from .serializers import NewsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class NewsListView(ListView):
    template_name = 'news/list.html'
    queryset = NewsModel.objects.all().order_by('-publish')
    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'news/detail.html'
    context_object_name = 'news'


class NewsEditView(LoginRequiredMixin, FormView):
    template_name = 'news/create.html'
    form_class = NewsForm
    success_url = reverse_lazy('news:list')

    def post(self, request, *args, **kwargs):
        form = NewsForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.slug = slugify(unidecode(new_form.title))
            new_form.save()
            return super().post(request, *args, **kwargs)


# API
# @api_view(['GET', "POST"])
# def api_news(request):
#     if request.method == 'GET':
#         news = NewsModel.objects.all()
#         serializer = NewsSerializer(news, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = NewsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)

class ApiNewsAllAndCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        news = NewsModel.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'PATCH', "DELETE"])
# def api_news_detail(request, slug):
#     news = NewsModel.objects.get(slug=slug)

#     if request.method == 'GET':
#         serializer = NewsSerializer(news)
#         return Response(serializer.data)
#     elif  request.method == "PATCH":
#         serializer = NewsSerializer(news, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         news.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ApiNewsMethods(APIView):

    def get(self, request, slug):
        news = NewsModel.objects.get(slug=slug)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,  request, slug):
        news = NewsModel.objects.get(slug=slug)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,  request, slug):
        news = NewsModel.objects.get(slug=slug)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        news = NewsModel.objects.get(slug=slug)
        news.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
