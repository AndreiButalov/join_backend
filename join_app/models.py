from django.db import models
from django.utils import timezone

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
    name = models.TextField(default="")
    color = models.TextField(default="")
    date = models.DateField(default=timezone.localdate)
    description = models.TextField(null=True, blank=True)
    initial = models.TextField(default="") 
    priority = models.CharField(max_length=20, default="Medium")    
    priorityImg = models.TextField(default="./assets/img/vector_strich.svg") 
    status = models.CharField(max_length=20)
    title = models.CharField(255)
    assignedTo = models.TextField(default="")
    category = models.CharField(max_length=20, null=True, blank=True)
    subtasks = models.TextField(default="")
    selectedTask = models.TextField(default="")



from django.db import models
from django.utils import timezone

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
    name = models.TextField(default="")
    color = models.TextField(default="")
    date = models.DateField(default=timezone.localdate)
    description = models.TextField(null=True, blank=True)
    initial = models.TextField(default="") 
    priority = models.CharField(max_length=20, default="Medium")    
    priorityImg = models.TextField(default="./assets/img/vector_strich.svg") 
    status = models.CharField(max_length=20)
    title = models.CharField(255)
    assignedTo = models.TextField(default="")
    category = models.CharField(max_length=20, null=True, blank=True)
    subtasks = models.TextField(default="")
    selectedTask = models.TextField(default="")

