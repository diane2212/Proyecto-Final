from django.views.generic import TemplateView
from apps.post.models import Post
#desde las vistas generales que tiene django...
#vistas basadas en clases, o en funciones
class IndexView(TemplateView):
    model= Post
    template_name = "index.html"
    context_object_name= 'posts'
    paginate_by= 3

    def queryset(self):
        return Post.objects.all().order_by('-creation_date')
    
class AboutView(TemplateView):
    template_name= 'about.html'