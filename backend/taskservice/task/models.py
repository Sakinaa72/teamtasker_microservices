from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    assigned_to=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.IntegerField()

    