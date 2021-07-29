from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Для активации нового пользователя
from .dispatch.user_register_dispatch import signer
from django.core.signing import BadSignature

# Для смены пароля
from django.contrib.auth.views import PasswordChangeView

# Для сброса пароля
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView)

from .models import AdvUser
from .forms import AdvUserRegisterForm, UpdateUserForm

# Для вывода сообщений
from django.contrib.messages.views import SuccessMessageMixin


class AdvUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    models = AdvUser
    success_url = reverse_lazy('main:index')


class AdvUserLogouView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'


class AdvUserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    model = AdvUser
    form_class = AdvUserRegisterForm
    success_url = reverse_lazy('users:login')
    success_message = 'Для завершения регистрации, активируйте свой аккаунт, \
                       перейдя по ссылке в письме.'


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class UpdateUserView(UpdateView):
    form_class = UpdateUserForm
    model = AdvUser
    success_url = reverse_lazy('users:profile')
    template_name = 'accounts/update.html'


# Смена пароля
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('users:profile')


# Для сброса пароля
class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('users:password_reset_done')
    subject_template_name = 'email/subject.txt'
    email_template_name = 'email/email.txt'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


def register_activate(request, token):
    try:
        username = signer.unsign(token)
    except BadSignature:
        return render(request, 'accounts/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_active:
        template = 'accounts/user_is_active.html'
    else:
        template = 'accounts/activation_done.html'
        user.is_active = True
        user.save()
    return render(request, template)
