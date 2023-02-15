from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
# from django import forms
from .models import User


# class LoginForm(AuthenticationForm):
#     email = forms.EmailField(label='Email / Username')

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
