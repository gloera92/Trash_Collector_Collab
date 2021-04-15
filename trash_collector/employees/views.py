from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,reverse
from django.apps import apps
from .models import Employees
import datetime
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.
my_date = datetime.datetime.now()
todays_day = my_date.isoweekday()
if todays_day == 1:
    the_day = "Monday"
elif todays_day == 2:
    the_day = "Tuesday"
elif todays_day == 3:
    the_day = "Wednesday"
elif todays_day == 4:
    the_day = "Thursday"
elif todays_day == 5:
    the_day = "Friday"
elif todays_day == 6:
    the_day = "Saturday"
elif todays_day == 7:
    the_day = "Sunday"


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    user = request.user
    if Employees.objects.filter(user=request.user).exists():
        employee = Employees.objects.get(user=request.user)
        all_customers = Customer.objects.all()
        zip_c = all_customers.filter(zip_code=employee.zip_code)
        customer = zip_c.filter(pickup_date=the_day)
        context = {
            'Employee': employee, 'Customer': customer
            }
        return render(request, 'employees/index.html', context)

    else:
        return render(request, 'employees/create.html')


def todays_pickup(request):
    if request.method == 'POST':
        pickup = request.POST.get('Todays_Pickup')
        Customer = apps.get_model('customers.Customer')
        all_customers = Customer.objects.all()
        employee_customers = all_customers.filter(pickup_date=pickup)
        context = {
            'employee_customers': employee_customers
        }
        return render(request, 'employees/todays_customers.html', context)
    else:
        return render(request, 'employees/todays_pickup.html')


def create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employees(name=name, user=request.user, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


def confirm(request, customer_id):
    if request.method == 'GET':
        Customer = apps.get_model('customers.Customer')
        customer = Customer.objects.get(pk=customer_id)
        customer.amount_owed += 25
        customer.confirmed = True
        customer.save()
        return render(request, 'employees/confirm.html')
    else:
        return render(request, 'employees/todays_customers.html')


def account_info(request):
    user = Employees.objects.get(user_id=request.user)
    context = {
        'Employees': user
    }
    return render(request, 'employees/account_info.html', context)