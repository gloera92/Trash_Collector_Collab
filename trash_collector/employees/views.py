from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,reverse
from django.apps import apps
from .models import Employees
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    user = request.user
    if Employees.objects.filter(user=request.user).exists():
        print(user)
        return render(request, 'employees/index.html')

    else:
        return render(request, 'employees/create.html')


def todays_pickup(request):
    if request.method == "GET":

        Customer = apps.get_model('customers.Customer')
        employee = Employees.objects.get(pk=1)
        context = {
            'employee': employee
        }
    return render(request, 'employees/todays_pickup.html', context)


def create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employees(name=name, user=request.user, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')
