from django.http import HttpResponse, HttpResponseRedirect
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
    user_id = customer_id
    pickup = Customer.objects.get(pk=user_id)
    context = {
        'Customer': pickup
    }
    return render(request, 'customers/pickup.html', context)


def create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.POST.get('user')
        pick_up_date = request.POST.get('pick_up_date')
        suspend_start = request.POST.get('suspend_start')
        suspend_end = request.POST.get('suspend_end')
        amount_owed = request.POST.get('amount_owed')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        new_customer = Customer(name=name, user=user, pick_up_date=pick_up_date, suspend_start=suspend_start, suspend_end=suspend_end, amount_owed=amount_owed, address=address, zip_code=zip_code)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')
