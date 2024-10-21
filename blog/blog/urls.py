"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include 
from django.conf import settings
from blog.views import IndexView, AboutView #desde el archivo blog-views importar la clase indexview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="home"), #avisar a django que hay una vista basada en clases
    path("about-us/", AboutView.as_view(), name="about"),
    path("", include("apps.post.urls")),
    path("", include("apps.user.urls")),
     path("", include("apps.contacto.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root= settings.MEDIA_ROOT)

