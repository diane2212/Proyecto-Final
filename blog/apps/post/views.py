from django.views.generic import TemplateView, ListView, DetailView, CreateView
from apps.post.models import Post, PostImage
from apps.post.forms import NewPostForm
from django.urls import reverse
from django.conf import settings

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name= "post/post_list.html"
    context_object_name = "object_list"

  #Creamos la vista PostCreateView que hereda de CreateView la cual nos permite crear un objeto de
  #un modelo en una vista.

class PostCreateView(CreateView):
    model= Post
    form_class= NewPostForm
    template_name= "post/post_create.html"
    
    def form_valid(self, form):
        form.instance.author= self.request.user
        post= form.save()

        images= self.request.FILES.getlist("images")
        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        else:
            PostImage.objects.create(post=post, image=settings.DEFAULT_POST_IMAGE)

        return super().form_valid(form)

         #esta funcion dirige a la vista de detalle del post
    def get_success_url(self):
        return reverse("post:post_detail", kwargs={'slug':self.objects.slug})
    

class PostDetailView(DetailView):
    model= Post
    template_name= "post/post_detail.html"
    context_object_name = "post"



class PostUpdateView(TemplateView):
    template_name = "post/post_update.html"

class PostDeleteView(TemplateView):
    template_name = "post/post_delete.html"
