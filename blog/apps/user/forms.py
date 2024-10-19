#aca crearemos el formulario para registro de los usuarios

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.user.models import User

class RegisterForm(UserCreationForm):
 
  fields = ('username', 'password', 'email', 'alias', 'avatar')
  username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'style': 'border-radius: 10px' 'bg-blue-500' 'box-sizing: border-box'}))
  password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'style': 'border-radius: 10px' 'bg-blue-500'}))
  email = forms.CharField(label='Email',widget=forms.TextInput(attrs={'style': 'border-radius: 10px' 'bg-blue-500' 'box-sizing: border-box'}))
  alias= forms.CharField(label='Alias',widget=forms.TextInput(attrs={'style': 'border-radius: 10px' 'bg-blue-500'  'box-sizing: border-box'}))                                    
                                            
                                            
                                   

class LoginForm(AuthenticationForm):
   username = forms.CharField( max_length=254, label='Usuario',widget=forms.TextInput(
        attrs={'style': 'border-radius: 10px' 'bg-blue-500'}))
   password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={'style': 'border-radius: 10px' 'bg-blue-500'}))

