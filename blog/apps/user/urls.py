from django.urls import path #se utiliza para definir las rutas
import apps.user.views as views #para acceder a las visas definididas

app_name = "user" #crear una vista de un perfil de usuario

urlpatterns = [
    path("users/profile/", views.UserProfileView.as_view(), name="user_profile"),
]