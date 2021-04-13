from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='create_new_customer'),
    path('pickup/', views.pickup_day, name='pickup'),
    path('change_day/', views.change_day, name='change_day'),
    path('start_end_day/', views.suspend_start_day, name='start_end_day'),
    path('one_time_pickup/', views.one_time_pickup, name='one_time_pickup'),
    path('account_info/', views.account_info, name='account_info'),
    path('', views.amount_owed, name='amount_owed')
]
