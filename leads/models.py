from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
    pass



class Agent(models.Model):
    # first_name=models.CharField(max_length=20)
    # last_name=models.CharField(max_length=20)
    # (WE DONT HAVE TO PUT FIRST_NAME AND LAST_NAME IN HERE bcos
    # AbstractUser can have them bydefault)


    # it makes one user can have one agent only
    # if we provide foreign key
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    # it makes one user can have many agents which is niot correct
    # here the suitable field is OneToOneField only
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class Lead(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    agent=models.ForeignKey(Agent,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

