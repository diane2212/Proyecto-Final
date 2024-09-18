from django.shortcuts import render
from blog.user import TemplateView

# Create your views here.
class UserProfileView(TemplateView):
    template_name =