from django.urls import path #se utiliza para definir las rutas
import apps.user.views as views #para acceder a las visas definididas

app_name = "user" #crear una vista de un perfil de usuario

urlpatterns = [
    path("users/profile/", views.UserProfileView.as_view(), name="user_profile"),
    path("users/login/", views.UserLoginView.as_view(), name="user_login"),
    path("users/signup/", views.UserSignupView.as_view(), name="user_signup"),
    path('auth/register/', views.RegisterView.as_view(), name="auth_register"),
    path('auth/login/', views.UserLoginView.as_view(), name="auth_login"),
    path('auth/logout/', views.LogoutView.as_view(), name="auth_logout"),
]
