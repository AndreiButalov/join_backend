from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    email = models.EmailField()
    passwort = models.TextField()

    def __str__(self):
        return self.name


class GuestContacts(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.TextField()



class Tasks(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    initial = models.TextField() 
    priotity = models.CharField(20)    
    priorityImg = models.TextField()
    status = models.CharField(20)
    title = models.CharField(255)
    assignedTo = models.TextField()
