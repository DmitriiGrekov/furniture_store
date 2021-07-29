from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from .models import AdvUser
from .dispatch.user_register_dispatch import user_reg_ds


class AdvUserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль',
                                widget=forms.widgets.PasswordInput(),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль(повторно)',
                                widget=forms.widgets.PasswordInput())
    phone = forms.CharField(max_length=20, label='Телефон',
                            widget=forms.widgets.TextInput())
    avatar = forms.ImageField(label='Аватар')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data['password2']
        user = get_user_model()
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError("Введенные пароль не совпадают", code='password_mismathc')}
            raise ValidationError(errors)
        if user.objects.filter(email=self.cleaned_data.get('email')).exists():
            errors = {'email': ValidationError('Введенный email уже существует')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user_reg_ds.send(sender=self.__class__, user=user)
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'phone',
                  'avatar',
                  'password1',
                  'password2')


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'avatar')


class PasswordChangeForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль',
                                widget=forms.widgets.PasswordInput(),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль(повторно)',
                                widget=forms.widgets.PasswordInput())

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    class Meta:
        model = AdvUser
        fields = ('password1', 'password2')
