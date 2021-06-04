from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid 
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to = 'profile_pictures')
    id = models.UUIDField(default= uuid.uuid4, primary_key= True, unique= True, editable= False)
    
    
    def __str__(self):
        return  f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)        


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
