from django.urls import path
from .views import company_view, create_review_view
from .views import ReviewsList, ReviewsDetail

app_name = 'company'
urlpatterns = [
    path('<slug:slug>/', company_view, name='company'),
    path('otzyvy/all/', ReviewsList.as_view(), name='otzyvy'),
    path('otzyvy/detail/<slug:slug>',
         ReviewsDetail.as_view(),
         name='detail_review'),
    path('create/review/', create_review_view, name='create'),
]
