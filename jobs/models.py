from django.db import models

# Create your models here.
class Jobs(models.Model):
    title=models.CharField(max_length=50)
    summary=models.TextField()
