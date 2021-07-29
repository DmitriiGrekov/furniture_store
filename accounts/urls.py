from django.urls import path
from .views import AdvUserLoginView, AdvUserLogouView, AdvUserRegisterView
from .views import UserPasswordChangeView, UserPasswordResetView
from .views import ProfileView, UpdateUserView
from .views import UserPasswordResetCompleteView
from .views import UserPasswordResetConfirmView
from .views import UserPasswordResetDoneView
from .views import register_activate


app_name = 'users'
urlpatterns = [
    path('login/', AdvUserLoginView.as_view(), name='login'),
    path('logout/', AdvUserLogouView.as_view(), name='logout'),
    path('register/', AdvUserRegisterView.as_view(), name='register'),
    path('register_done/<str:token>/', register_activate,
         name='register_activate'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update/<int:pk>', UpdateUserView.as_view(), name='update'),
    path('change_password/', UserPasswordChangeView.as_view(),
         name='password_change'),
    path('password_reset/', UserPasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<token>',
         UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/complete/', UserPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
