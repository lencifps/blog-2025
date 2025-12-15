from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from apps.user.models import User



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'bg-blue-50', 'placeholder': 'Usuario'}
    ))

    password = forms.CharField(max_length=150, widget=forms.PasswordInput(
        attrs={'class': 'bg-red-50', 'placeholder': 'Contraseña'}
    ))
    
    