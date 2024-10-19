from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from apps.post.models import Post, PostImage, Comment
from django.db.models import Count
from apps.post.forms import NewPostForm, UpdatePostForm, CommentForm, PostFilterForm
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.shortcuts import get_object_or_404

class PostListView(ListView):
    model = Post
    template_name= 'post/post_list.html'
    context_object_name = "posts"
    paginate_by= 10 #definimos mostrar 10 post por pagina

    def get_queryset(self):
        queryset = Post.objects.all().annotate(comments_count=Count('comments')) 
        # Anotamos la cantidad de comentarios en cada post
        search_query = self.request.GET.get('search_query', '')
        order_by = self.request.GET.get('order_by', '-creation_date')

        # Filtramos por título o autor si se proporciona una búsqueda
        if search_query:
           queryset = queryset.filter(title__icontains=search_query)
           queryset.filter(author__username__icontains=search_query)
        return queryset.order_by(order_by)
    
       
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = PostFilterForm(self.request.GET) # Pasamos el formulario de filtro al contexto

         # Manejamos la paginación
        if context.get('is_paginated', False):
           query_params = self.request.GET.copy()
           query_params.pop('page', None)
           pagination = {}
           page_obj = context['page_obj']
           paginator = context['paginator']
           # Usamos number para obtener el número de la página actual
           if page_obj.number > 1:
              pagination['first_page'] = f'?{query_params.urlencode()}&page={paginator.page_range[0]}'
              
              # Usamos has_previous para saber si hay una página anterior
           if page_obj.has_previous():
              pagination['previous_page'] = f'?{query_params.urlencode()}&page={page_obj.number - 1}'
              # Usamos has_next para saber si hay una página siguiente
           if page_obj.has_next():
              pagination['next_page'] = f'?{query_params.urlencode()}&page={page_obj.number + 1}'

              # Usamos num_pages para obtener el número total de páginas
           if page_obj.number < paginator.num_pages:
              pagination['last_page'] = f'?{query_params.urlencode()}&page={paginator.num_pages}'
              context['pagination'] = pagination
        return context



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
        return reverse("post:post_detail", kwargs={'slug':self.object.slug})
    

class PostDetailView(DetailView):
    model= Post
    template_name= 'post/post_detail.html'
    context_object_name = "post"
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener todas las imágenes activas del post
        active_images = self.object.images.filter(active=True)

        context['active_images'] = active_images
        context['add_comment_form'] = CommentForm()
        
        #editar un comentario
        edit_comment_id= self.request.GET.get('edit_comment')
        if edit_comment_id:
            comment= get_object_or_404(Comment, id= edit_comment_id)
            #si el usuario quiere editar un commentario y esta registrado mostrar/Sino
            if comment.author== self.request.user: 
                context['editing_comment_id']= comment.id
                context['edit_comment_form']= CommentForm(instance=comment)
            else:
                context['editing_comment_id']= None
                context['edit_comment_form']= None

        return context


class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'post/post_update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['active_images'] = self.get_object().images.filter(active=True) # Pasamos las imágenes activas
        return kwargs


    def form_valid(self, form):
        post = form.save(commit=False)
        active_images = form.active_images
        keep_any_image_active = False

        if active_images:
         for image in active_images:
            field_name = f"keep_image_{image.id}"
             # Si el checkbox no está marcado, eliminamos la imagen
            if not form.cleaned_data.get(field_name, True):
                image.active = False
                image.save()
            else:
                 keep_any_image_active = True

        
        images = self.request.FILES.getlist('images')
        if images:
           for image in images:
             PostImage.objects.create(post=post, image=image)
   
        if not keep_any_image_active and not images:
            PostImage.objects.create(post=post, image=settings.DEFAULT_POST_IMAGE)
        post.save() 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post:post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(DeleteView):
    model= Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post:post_list')

class CommentCreateView(CreateView):
      model= Comment
      form_class= CommentForm
      template_name= 'post/post_detail.html' #usa el template de post detail

      def form_valid(self, form):
          form.instance.author = self.request.user
          form.instance.post= Post.objects.get(slug= self.kwargs['slug'])
          return super().form_valid(form) 
           
      def get_success_url(self):
          return reverse_lazy('post:post_detail', kwargs= {'slug': self.object.post.slug})

class CommentUpdateView(UpdateView):
    model= Comment
    form_class= CommentForm
    template_name= 'post/post_detail.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post:post_detail', kwargs={'slug': self.object.post.slug})
     #test_func permite validar el usuario
    def test_func(self):
        comment= self.get_object()
        return comment.author == self.request.user

class CommentDeleteView(DeleteView):
    pass

