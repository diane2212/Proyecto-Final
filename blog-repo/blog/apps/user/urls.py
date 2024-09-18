from django.urls import render
from blog.views import TemplateView

class UserProfileView(TemplateView):
    template_name = 