from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL
class Story(models.Model):
    topic = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.topic