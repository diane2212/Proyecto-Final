from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
import uuid
import os

class Post(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   title = models.CharField(max_length=200)
   time = models.CharField(max_length=200, null= True, blank= True )
   slug = models.SlugField(unique=True, max_length=200, blank=True)
   content = models.TextField(max_length=10000)
   author = models.ForeignKey(
   settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   creation_date = models.DateTimeField(default=timezone.now)
   modification_date = models.DateTimeField(auto_now=True)
   allow_comments = models.BooleanField(default=True)
   category= models.ForeignKey('Category', on_delete= models.CASCADE, null= True, blank= True, related_name="posts")

   #str es como --init--
   def __str__(self):
      return self.title

   @property
     #decorador de la funcion
   def amount_comments(self):
      return self.comments.count()
     # TODO: DEFINIR COMENTARIOS

   @property
   def amount_images(self):
      return self.images.count()
   
   def save(self, *args, **kwargs):
       if not self.slug:
         self.slug = self.generate_unique_slug()
       super().save(*args, **kwargs)

   def generate_unique_slug(self):
      # tenemos este titulo para el post
      # tenemos-este-titulo-para-el-post
      # tenemos-este-titulo-para-el-post-1
      # tenemos-este-titulo-para-el-post-2
      # tenemos-este-titulo-para-el-post-3
      slug = slugify(self.title)
      unique_slug = slug
      num = 1
   
   
      while Post.objects.filter(slug=unique_slug).exists():
         unique_slug = f'{slug}-{num}'
         num += 1
      return unique_slug


def get_image_filename(instance, filename):
   post_id = instance.post.id
   images_count = instance.post.images.count()
   base_filename, file_extension = os.path.splitext(filename) #esto se llama unpacking
   new_filename = f"post_{post_id}_cover_{images_count + 1}{file_extension}"
   return os.path.join("post/cover/", new_filename)

class PostImage(models.Model):
   post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "images")
   image = models.ImageField(upload_to = get_image_filename, default=settings.DEFAULT_POST_IMAGE)
   active= models.BooleanField (default= True)

   def __str__(self):
      return f"PostImage {self.id}"

 
class Comment(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   content = models.TextField(max_length=500)
   creation_date = models.DateTimeField(auto_now_add=True)
   author = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
   post = models.ForeignKey(
      Post, on_delete=models.CASCADE, related_name='comments')

   def __str__(self):
    return self.content
   

class Category(models.Model):
   id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
   title=models.CharField(max_length=200)
   post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name="category_posts")

   def __str__(self):
      return self.title
   