from django.db import models

# Create your models here.
class Profile(models.Model):
    user_id=models.IntegerField(unique=True)
    role=models.CharField(max_length=50, default='user')
    bio=models.TextField(blank=True)
    