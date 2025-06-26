from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Vendor, Car
from .forms import CustomUserCreationForm, CarForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Renombramos para evitar conflicto
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home (request):
    cars = Car.objects.all().order_by('name', 'price', 'published_date')
    return render(request, "base/home.html", {'cars': cars})

def cargest(request):
    return render(request, "car_gest/available_cars.html")

def cars(request):
    cars = Car.objects.all().order_by('name', 'price', 'published_date')
    return render(request, 'base/home.html', {'cars': cars})

@login_required
def sell_cars(request):
    vendor, created = Vendor.objects.get_or_create(user=request.user)  # Desempaqueta la tupla
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)  # Añadí request.FILES por si recibes archivos

        if car_form.is_valid():
            car = car_form.save(commit=False)
            car.vendor = vendor  # Asigna solo el objeto Vendor, no la tupla
            car.save()
            return redirect('cargest/', pk=car.pk)  # Verifica que 'cargest/' sea el nombre correcto de tu URL
    else:
        car_form = CarForm()
    
    return render(request, 'car_gest/sell_car.html', {
        'car_form': car_form,
    })

def cars_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car_gest/cars_details.html', {'car': car})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('/')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'car_gest/log_in.html')

def log_out(request):
    logout(request)
    return redirect('home')

def sign_up(request):  
   if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
        else:
            messages.error(request, 'Por favor, corriga los erroes debajo.')
   else:
        form = CustomUserCreationForm()

   return render(request, 'car_gest/sign_up.html', {'form': form})

