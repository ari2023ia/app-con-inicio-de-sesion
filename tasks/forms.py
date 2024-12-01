from django import forms
from .models import CustomUser, Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

class EditAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('nombre_de_usuario', 'correo_electronico')

class RegisterForm(UserCreationForm):
    correo_electronico = forms.EmailField(label='Correo electrónico')

    class Meta:
        model = CustomUser
        fields = ('nombre_de_usuario', 'correo_electronico', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    nombre_de_usuario = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'content')

class LoginForm(forms.Form):
    nombre_de_usuario = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        nombre_de_usuario = cleaned_data.get('nombre_de_usuario')
        password = cleaned_data.get('password')

        if nombre_de_usuario and password:
            user = authenticate(nombre_de_usuario=nombre_de_usuario, password=password)
            if not user:
                self.add_error('password', 'Contraseña incorrecta')
            elif not user.is_active:
                self.add_error('nombre_de_usuario', 'Cuenta desactivada')
        return cleaned_data

class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('password',)
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'content')