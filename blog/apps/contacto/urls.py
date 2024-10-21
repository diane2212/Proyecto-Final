from django.urls import path
import apps.contacto.views as views

app_name = 'apps.contacto'

urlpatterns = [
    path('contacto/', views.ContactoUsuario.as_view(), name='contacto'),
]
