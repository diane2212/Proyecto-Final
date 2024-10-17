from django.shortcuts import render
from blog.views import TemplateView
from django.contrib.auth.views import LoginView as LoginViewDjango, LogoutView as LogoutViewDjango
from django.views.generic import TemplateView, CreateView
from apps.user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy

class UserProfileView(TemplateView):
    template_name = 'user/user_profile.html'
#una view para registrarse
class RegisterView(CreateView):
   template_name = 'auth/auth_register.html'
   form_class = RegisterForm
   success_url = reverse_lazy('home') # Redirige al home una vez registrado
 
   def form_valid(self, form):
     # Llama a la función form_valid de la clase padre y guarda el usuario
       response = super().form_valid(form)


     # Asignar el grupo Registered al usuario recién creado
       registered_group = Group.objects.get(name='Registered')
       self.object.groups.add(registered_group)
     # En caso de ser necesario se le puede asignar explicitamente los permisos del grupo al usuario
     # for permission in registered_group.permissions.all():
     # self.object.user_permissions.add(permission)
       return response
#una view para iniciar sesion
class UserLoginView(LoginViewDjango):
   template_name = 'auth/auth_login.html'
   authentication_form = LoginForm

   def get_success_url(self):
    return reverse_lazy('home')
#view para cerrar sesion
class LogoutView(LogoutViewDjango):
 
   def get_success_url(self):
     return reverse_lazy('home')

class UserSignupView(TemplateView):
    template_name = "user/user_signup.html"