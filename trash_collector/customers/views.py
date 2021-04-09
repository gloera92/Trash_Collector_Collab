from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # get the logged in user within any view function
    user = request.user
    # This will be useful while creating a customer to assign the logged in user as the user foreign key
    # Will also be useful in any function that needs
    print(user)
    return render(request, 'customers/index.html')


def pickup_day(request, customer_id):
    pickup = Customer.objects.get(pk=customer_id)
    context = {
        'pickup': pickup
    }
    return render(request, 'customers/pickup.html', context)
