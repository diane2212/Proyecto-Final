from django import forms
from apps.post.models import Post, PostImage, Comment

#El formulario PostForm hereda de forms.ModelForm y nos sirve de base tanto para crear como para
#actualizar un post.
#Por eso luego definimos un formulario NewPostForm que hereda de PostForm y agrega un campo
#image de tipo forms.ImageField. Además, definimos un método save que guarda la imagen en la
#base de datos.


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'content', 'allow_comments')

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
         'content': 'Comentario'
      }
      
      widgets= {
         'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe un comentario...', 'class': 'p-2'})
      }