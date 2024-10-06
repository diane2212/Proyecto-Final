from django import forms
from apps.post.models import Post, PostImage

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
       post= super().save(commit=False)#para que no se guarde en la Base de d
       image= self.cleaned_data["image"] 

       
       if commit:
          post.save()
          if image:
             PostImage.objects.create(post=post, image=self.cleaned_data["image"])
       return post
    
class UpdatePostForm(PostForm):
         pass