from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField(blank=True, null=True, upload_to='photos')
    email = models.EmailField()
    age = models.PositiveIntegerField(blank=True, null=True)



    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
