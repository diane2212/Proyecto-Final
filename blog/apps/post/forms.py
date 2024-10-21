from django import forms
from apps.post.models import Post, PostImage, Comment, Category



class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'time', 'category', 'content', 'allow_comments')

    labels= {
         'title': 'Titulo ',
         'time': 'Tiempo de preparacion ',
         'category': 'Categoria ',
         'content': 'Contenido ',
         'allow_comments': 'Comentarios '
    }

    widgets= {
         'title': forms.Textarea(attrs={'class': 'w-50 inline-block','rows': 1,
                                            'style': 'resize:none; border-radius: 10px; box-sizing: border-box; overflow-x:hidden;',
                                             'oninput': 'this.style.height= "";this.style.height=this.scrollHeight+"px";'}),
         'time' :forms.Textarea(attrs={'class': 'w-50 inline-block','rows': 1,
                                            'style': 'resize:none; border-radius: 10px; box-sizing: border-box; overflow-x:hidden;',
                                             'oninput': 'this.style.height= "";this.style.height=this.scrollHeight+"px";'}),
         'content' :forms.Textarea(attrs={'class': 'w-100 inline-block','rows': 5,
                                            'style': 'resize:none; border-radius: 10px; box-sizing: border-box; overflow-x:hidden;',
                                             'oninput': 'this.style.height= "";this.style.height=this.scrollHeight+"px";'})
      }

class NewPostForm(PostForm):
    image= forms.ImageField(required=False)
    
    def save(self, commit= True):
       ## Guardar el post pero no aún en la base de datos ya que necesitamos el id del post para la imagen
       post= super().save(commit=False)#para que no se guarde en la Base de d 
       
       if commit:
          post.save()
       if self.cleaned_data["image"] :
          PostImage.objects.create(post=post, image=self.cleaned_data["image"])
       return post
    
class UpdatePostForm(PostForm):

   image = forms.ImageField(required=False)
     
   def __init__(self, *args, **kwargs):
     # Obtenemos las imágenes activas del post que se quiere actualizar
      self.active_images = kwargs.pop('active_images', None)
      super(UpdatePostForm, self).__init__(*args, **kwargs)
 
      if self.active_images:
       for image in self.active_images:
           # keep_image_1, keep_image_2,nombre del campo que se creará en el formulario para mantener la imagen activa
           field_name = f"keep_image_{image.id}" 
           self.fields[field_name] = forms.BooleanField(required=False, initial=True, label=f"Mantener {image}")


   def save(self, commit=True):
     post = super().save(commit=False)
     if commit:
         post.save()
         if self.cleaned_data['image']: # Si el usuario sube una nueva imagen
            PostImage.objects.create(post=post, image=self.cleaned_data['image'])
            if self.active_images: # Si hay imágenes activas y se quiere mantener alguna
        
               for image in self.active_images:
                   if not self.cleaned_data.get(f"keep_image_{image.id}", True):
                     image.delete() # Eliminar la imagen si el usuario no la quiere mantener, checkboxes desmarcados
     return post


class CommentForm(forms.ModelForm):
   class Meta:
      model= Comment
      fields= ['content']

      labels= {
         'content': ''
      }
      
      widgets= {
         'content': forms.Textarea(attrs={'placeholder': '  Escribe un comentario...', 
                                          'class': 'w-50 inline-block','rows': 1,
                                            'style': 'resize:none; border-radius: 10px; box-sizing: border-box; overflow-x:hidden;',
                                             'oninput': 'this.style.height= "";this.style.height=this.scrollHeight+"px";'})
      }

class PostFilterForm(forms.Form):
   search_query = forms.CharField(required= False,widget=forms.TextInput(attrs={'placeholder': '  Buscar...', 'class':'bg-gray-100' 'w-full sm:w-[400px]',
                                                                                 'style': 'border-radius: 10px'}))
   order_by= forms.ChoiceField( required=False,
      choices=(
       ('', 'Ordenar por'),
       ('-creation_date', 'Mas reciente'),
       ('creation_date', 'Mas antiguo'),
       ('-comments_count', 'Mas comentado'),
       ('comments_count', 'Menos comentados'),
       ('title', 'Titulos (A-Z)'),
       ('-title', 'Titulos (Z,A)')
      ),
       widget=forms.Select(attrs={'class':'bg-gray-100' 'w-full' 'p-2',  'style': 'border-radius: 10px' })
   )
   
   category= forms.ModelChoiceField(queryset=Category.objects.all(),required= False,empty_label= 'Filtrar por',
                                    widget=forms.Select(attrs={'class':'bg-gray-100' 'w-full' 'p-2',  'style': 'border-radius: 10px', 'onchange':'this.form.submit();' })
   )  