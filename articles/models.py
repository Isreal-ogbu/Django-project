from django.db import models

# Create your models here.
class Articles(models.Model):
    name = models.TextField()
    details = models.TextField()
    