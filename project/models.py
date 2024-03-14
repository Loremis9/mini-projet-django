from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Leaves(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ManyToManyField(User, default="")


class Statu(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Projet(models.Model):
    name = models.CharField(max_length=50,default='valeur')
    start_date = models.DateField()
    end_date = models.DateField()
    # status_id foreign_key
    status = models.ForeignKey(Statu, on_delete=models.CASCADE, default="1")
    # manager_id foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.name


class Task(models.Model):
    # id projet foreign key
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, default=0)
    subtaskof = models.IntegerField()
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=500)
    # task_owner foreign_key user
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    # status_id foreign_key
    status = models.ForeignKey(Statu, on_delete=models.CASCADE,default="1")
    start_date = models.DateField()
    duration = models.IntegerField()
    completion_rate = models.DecimalField(max_length=100,decimal_places=2,max_digits=3)

    def __str__(self):
        return self.task_name



"""
models qui sert aux vacances congès maladie etc ...
"""


