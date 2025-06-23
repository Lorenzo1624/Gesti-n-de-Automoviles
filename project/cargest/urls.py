from django.contrib import admin
from . import views
from django.urls import path
from django.urls import include

urlpatterns= [
    path('', views.home, name='home'),
    path('log_in/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('cargest/', views.cars, name='cargest'),
    path('cargest/<int:car_id>/', views.cars_details, name='details'),
    path('sell', views.sell_cars, name='sell'),
  ]