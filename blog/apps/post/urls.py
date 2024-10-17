from django.urls import path
import apps.post.views as views #de apps-views.py importar todas las vistas

app_name = "post"

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name="post_list"),
    path('posts/create', views.PostCreateView.as_view(), name="post_create"),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name="post_detail"),
    path('posts/<slug:slug>/update', views.PostUpdateView.as_view(), name="post_update"),
    path('posts/<slug:slug>/delete', views.PostDeleteView.as_view(), name="post_delete"),
    path('posts/<slug:slug>/comments/create', views.CommentCreateView.as_view(), name="comment_create"),
    path('comments/<uuid:pk>/update', views.CommentUpdateView.as_view(), name="comment_update"),
    path('comments/<uuid:pk>/delete', views.CommentDeleteView.as_view(), name="comment_delete"),
]

#n este caso, se han definido las siguientes URLs:
#post_list: URL para listar los posts en ventana
#post_create: URL para crear un nuevo post.
#post_detail: URL para ver un post en detalle.
#post_update: URL para actualizar un post.
#post_delete: URL para eliminar un post
#