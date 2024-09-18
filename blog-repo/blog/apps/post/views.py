from django.shortcuts import render
from blog.views import TemplateView

# Create your views here.
class PostDetailView(TemplateView):
    template_name= "post/post_detail.html"
