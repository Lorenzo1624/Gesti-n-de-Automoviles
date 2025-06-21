from django.contrib import admin
from . import views
from django.urls import path
from django.urls import include

urlpatterns= [
    path('', views.home, name='home'),
    path('tuabuela/', views.tuabuela, name ='tuabuela'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('cargest/', views.cars, name='cargest'),
    path('cargest/<int:car_id>/', views.cars_details, name='details'),
    path('sell', views.sell_cars, name='sell'),
  ]