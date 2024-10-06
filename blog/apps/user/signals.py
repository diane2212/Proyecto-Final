from apps.user.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from apps.post.models import Post, Comment

#posterior a registrarse el usuario se va a ejecutar esta funcion
@receiver(post_save, sender=User)
#decoradores son funciones que rodean mi funcion que esta definida por debajo
def create_groups_and_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        try:
            post_content_type = ContentType.objects.get_for_model(Post)
            comment_content_type = ContentType.objects.get_for_model(Comment)
           #PERMISOS DE POST
            view_post_permission = Permission.objects.get(codename= "view_post", content_type = post_content_type)
            add_post_permission = Permission.objects.get(codename= "add_post", content_type = post_content_type)
            change_post_permission = Permission.objects.get(codename= "change_post", content_type = post_content_type)
            delete_post_permission = Permission.objects.get(codename= "delete_post", content_type = post_content_type)
           #PERMISOS DE COMENTARIOS
            view_comment_permission = Permission.objects.get(codename= "view_comment", content_type = comment_content_type)
            add_comment_permission = Permission.objects.get(codename= "add_comment", content_type = comment_content_type)
            change_comment_permission = Permission.objects.get(codename= "change_comment", content_type = comment_content_type)
            delete_comment_permission = Permission.objects.get(codename= "delete_comment", content_type = comment_content_type)
            #CREAMOS GRUPO DE USUARIOS REGISTRADOS
            registered_group, created = Group.objects.get_or_create(name="Registered")
            registered_group.permissions.add(
            view_post_permission,
            add_post_permission,
            change_post_permission,
            delete_post_permission,
            # TODO: tengo que ver que permisos voy a dejar
            view_comment_permission,
            add_comment_permission,
            change_comment_permission,
            delete_comment_permission
            )
           #CREAMOS GRUPO DE COLABORADORES
            registered_group, created = Group.objects.get_or_create(name="Collaborators")
            registered_group.permissions.add(
            view_post_permission,
            add_post_permission,
            change_post_permission,
            delete_post_permission,
            # TODO: tengo que ver que permisos voy a dejar
            view_comment_permission,
            add_comment_permission,
            change_comment_permission,
            delete_comment_permission
            )
            #CREAMOS GRUPO DE ADMINISTRADORES (tiene todos los permisos, ver)
            registered_group, created = Group.objects.get_or_create(name="Admins")
            registered_group.permissions.add(
            registered_group.permissions.set(Permission.objects.all())
            )

        except ContentType.DoesNotExist:
            print("El tipo de contenido aun no esta disponible.")
        except Permission.DoesNotExist:
            print("Uno o mas permisos no estan disponibles aun")