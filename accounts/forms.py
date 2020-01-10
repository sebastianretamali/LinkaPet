from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulary Usuario
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    username = forms.CharField(max_length=25, label='Nombre Usuario')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmar Contraseña')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
 
#Formulary Fundación
class UserForm(UserCreationForm):
     email = forms.EmailField(max_length=254, required=True)
     username = forms.CharField(label='Nombre Usuario')
     first_name = forms.CharField(max_length=25, label='Nombre')
     last_name = forms.CharField(max_length=25, label='Apellido', required=False)
     password1 = forms.CharField(widget=forms.PasswordInput(), label='Contraseña antigua')
     password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmar Contraseña')
     class Meta:
        model = User
        fields = [  'email', 'username', 'first_name', 'last_name']
        




