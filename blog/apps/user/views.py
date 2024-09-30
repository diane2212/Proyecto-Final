from django.shortcuts import render
from blog.views import TemplateView


#from django.views.generic import DetailView
#from .models import UserProfile 

#class UserPorfileView(DetailView)
#model = UserProfile
#template_name = "user/user_profile.html"

# Create your views here. crear una vista
class UserProfileView(TemplateView):
    template_name = "user/user_profile.html"