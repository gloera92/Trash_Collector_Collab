from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='create_new_employee'),
    path('todays_pickup/', views.todays_pickup, name='todays_pickup'),
    path('confirm/<int:customer_id>/', views.confirm, name='confirm')
]