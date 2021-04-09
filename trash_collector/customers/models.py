from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    pick_up_date = models.CharField(max_length=50)
    one_time_pickup = models.DateField(null=True, blank=True)
    suspend_start = models.DateField(null=True, blank=True)
    suspend_end = models.DateField(null=True, blank=True)
    amount_owed = models.IntegerField(default=0)
    address = models.CharField(default='main st', max_length=50)
    zip_code = models.CharField(default='11111', max_length=50)
