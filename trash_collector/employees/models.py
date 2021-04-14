from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories


class Employees(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=None, on_delete=models.CASCADE)
    zip_code = models.CharField(default='11111', max_length=50)

