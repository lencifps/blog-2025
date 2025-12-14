from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os

   
def get_avatar_filename(instance, filename):
    #   Generar un nombre unico para el avatar usando el uuid del usuario.
    #   asdasdasdasd.png  
     _, file_extension = os.path.splitext(filename)

     new_filename = f"user-{instance.id}-avatar{file_extension}"

    #   user/avatar/user-UUIDv4-avatar.png
     return os.path.join("user/avatar/", new_filename)
   


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=20, unique=True, null=False, blank=True)
    avatar = models.ImageField(
        upload_to=get_avatar_filename, default="user/default/avatar-default.png"
    )
  

    def __str__(self):
         return self.username
    
    def get_avatar_url(self):
        if self.avatar:
             return self.avatar.url
        
    
    @property
    def is_colaborador(self):
        return self.groups.filter(name="colaborador").exists()
    
    @property
    def is_registrado(self):
        return self.groups.filter(name="registrado").exists()
    
    @property
    def is_moderador(self):
        return self.groups.filter(name="moderador").exists()