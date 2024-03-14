from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

class projet(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    # status_id foreign_key
    # manager_id foreign key


class task(models.Model):
    # id projet foreign key
    subtaskof = models.IntegerField()
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=500)
    # task_owner foreign_key
    # status_id foreign_key
    start_date = models.DateField()
    duration = models.IntegerField()
    completion_rate = models.DecimalField(max_length=100,decimal_places=2,max_digits=3)


class user(models.Model):
    email = models.EmailField()
    is_manager = models.BooleanField(default=False)
#     projet_id foreign key

class statu(models.Model):
    name = models.CharField(max_length=150)

"""
models qui sert aux vacances congès maladie etc ...
"""
class leaves(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    # user_id foreign_key