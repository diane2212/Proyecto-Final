from django.contrib import admin
from apps.post.models import Post, PostImage, Comment, Category

# registrar los modelos post, comment, PostImage para gestionarlos desde el panel de admin

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "creation_date", "modification_date", "allow_comments")
    #campos a mostrar en la lista
    search_files = ("title", "content", "author_username", "id") 
    #Campos de busqueda
    prepopulated_fields= {"slug" : ("title",)}
    #autocompletar slug a partir del titulo
    list_filter = ("category", "author", "creation_date", "allow_comments") #lista filtrada
    ordering= ("-creation_date",) #ordenar por fecha de creacion descendente

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

class CommentAdmin(admin.ModelAdmin):
    list_display= ("content", "author", "post", "creation_date")
    search_fields= ("content", "author_username", "post_title", "id")
    list_filter = ("creation_date", "author")
    ordering = ("-creation_date", ) #el signo simboliza bajada, descenciente

def activate_images(modeladmin, request, queryset):
    updated= queryset.update(active= True)
    modeladmin.message_user(request, f"{updated} imagenes fueron activadas correctamente")
    activate_images.short_description =" activar imagenes seleccionadas"

def deactivate_images(modeladmin, request, queryset):
    updated= queryset.update(active= False)
    modeladmin.message_user(request, f"{updated} imagenes fueron desactivadas correctamente")
    deactivate_images.short_description = "Desactivar imagenes seleccionadas"

class PostImageAdmin(admin.ModelAdmin):
    list_display = ("post", "image", "active") #campos a mostrar en la lista
    #buscar por titulo del post ynombre de las imagen
    search_fields = ("post_title", "image")
    list_filter = ("active",) #filtros en la lista
    #agregar las acciones personalizadas
    actions= [activate_images, deactivate_images]

#Registrar los modelos en el admin
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostImage, PostImageAdmin)