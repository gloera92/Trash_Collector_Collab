from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Customer
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # get the logged in user within any view function
    user = request.user
    # This will be useful while creating a customer to assign the logged in user as the user foreign key
    # Will also be useful in any function that needs

    if Customer.objects.filter(user=request.user).exists():
        print(user)
        return render(request, 'customers/index.html')

    else:
        return render(request, 'customers/create.html')




def pickup_day(request):
    # we have request.user
    # need to query the customer table to find the customer object whose user_id
    # matches the id of request.user
    # Then, we have the customer who is using the application

    pickup = Customer.objects.get(user_id=request.user)
    context = {
        'Customer': pickup
    }
    return render(request, 'customers/pickup.html', context)


def create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        new_customer = Customer(name=name, user=request.user, address=address, zip_code=zip_code)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')


def change_day(request):
    if request.method == 'POST':
        user = Customer.objects.get(user_id=request.user)
        user.pickup_date = request.POST.get('Pickup Date')
        user.save()
        return HttpResponseRedirect(reverse('customers:pickup'))
    else:
        return render(request, 'customers/pickup.html')


def suspend_start_day(request):
    if request.method == 'POST':
        user = Customer.objects.get(user_id=request.user)
        user.suspend_start = request.POST.get('Suspend Start Date')
        user.save()
        return HttpResponseRedirect(reverse('customers:start_end_day'))
    else:
        return render(request, 'customers/start_end_day.html')


def suspend_end_day(request):
    if request.method == 'POST':
        user = Customer.objects.get(user_id=request.user)
        user.suspend_end = request.POST.get('Suspend End Date')
        user.save()
        return HttpResponseRedirect(reverse('customers:end_day'))
    else:
        return render(request, 'customers/start_end_day.html')
