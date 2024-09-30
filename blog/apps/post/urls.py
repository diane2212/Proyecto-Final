from django.urls import path
import apps.post.views as views #de apps-views.py importar todas las vistas

app_name = "post"

urlpatterns = [
    path("posts/<slug:slug>/detail", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<slug:slug>/update", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<slug:slug>/delete", views.PostDeleteView.as_view(), name="post_delete"),
]