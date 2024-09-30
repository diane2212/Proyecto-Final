from django.views.generic import TemplateView
#desde las vistas generales que tiene django...
#vistas basadas en clases, o en funciones
class IndexView(TemplateView):
    template_name = "index.html"