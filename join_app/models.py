from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.TextField()

    def __str__(self):
        return self.name

