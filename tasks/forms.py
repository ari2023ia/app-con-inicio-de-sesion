from django import forms
from .models import Usuario, Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'content')

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                self.add_error('password', 'Contraseña incorrecta')
            elif not user.is_active:
                self.add_error('username', 'Cuenta desactivada')
        return cleaned_data

class EditAccountForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email')

class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('password',)
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'content')