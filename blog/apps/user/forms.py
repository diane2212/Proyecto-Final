#aca crearemos el formulario para registro de los usuarios

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.user.models import User

class RegisterForm(UserCreationForm):
 class Meta:
  model = User
  fields = ('username', 'email', 'alias', 'avatar')

 widgets= {
         'username': forms.Textarea(attrs={'placeholder': 'Nombre de usuario', 'class': 'w-50 inline-block','rows': 1,
                                            'style': 'resize:none; border-radius: 10px; box-sizing: border-box; overflow-x:hidden;',
                                             'oninput': 'this.style.height= "";this.style.height=this.scrollHeight+"px";'}),
          'email': forms.Textarea(attrs={'placeholder': 'Email', 'class': 'w-50 inline-block','rows': 1,
                                            'style': 'resize:none; border-radius: 10px; box-sizing: border-box; overflow-x:hidden;',
                                             'oninput': 'this.style.height= "";this.style.height=this.scrollHeight+"px";'}),
          'alias': forms.Textarea(attrs={'placeholder' : 'Alias', 'class': 'w-50 inline-block','rows': 1,
                                            'style': 'resize:none; border-radius: 10px; box-sizing: border-box; overflow-x:hidden;',
                                             'oninput': 'this.style.height= "";this.style.height=this.scrollHeight+"px";'})
     }

class LoginForm(AuthenticationForm):
   username = forms.CharField( max_length=254, widget=forms.TextInput(
        attrs={'style': 'border-radius: 10px' 'bg-blue-500'}))
   password = forms.CharField(widget=forms.PasswordInput(
        attrs={'style': 'border-radius: 10px' 'bg-blue-500'}))

