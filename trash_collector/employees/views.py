from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


def todays_pickup(request):
    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all()
    employees_customers = all_customers.filter(pickup_date=all_customers)
    if employees_customers == 'Monday':
        print(Customer)
    else:
        return render(request, 'employees/todays_pickup.html')

