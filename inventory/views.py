from django.shortcuts import render, get_object_or_404, redirect
from . models import Car, Review
from . forms import inventoryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
    return render(request, 'auth/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})


def index(request):
    return render(request, 'home.html')


def all_cars(request):
    cars = Car.objects.filter(person=request.user)

    context = {
        'cars': cars
    }
    return render(request, 'inventory/cars.html', context)


@login_required
def add_new_car(request):
    if request.method == 'POST':
        form = inventoryForm(request.POST)
        if form.is_valid():
            newCar = form.save(commit=False)
            newCar.person = request.user
            newCar.save()
            return redirect('all_cars')
        else:
             print(form.errors)

    else:
        form = inventoryForm()

    context = {
        'form': form
    }
    return render(request, 'inventory/add_car.html', context)



def car_edit(request, id):
    car = get_object_or_404(Car, pk=id)
    print(car)

    if request.method == 'POST':
        form = inventoryForm(request.POST, instance=car)
        form.save()

    else:
        form = inventoryForm(instance=car)
    
    context = {
        'form': form,
    }
    return render(request, 'inventory/add_car.html', context)

def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    reviews = Review.objects.filter(car=car)

    context = {
        'car': car,
        'reviews': reviews
    }
    return render(request, 'inventory/car_detail.html', context)

def add_review(request, id):
    car = get_object_or_404(Car, pk=id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.save()

    else:
        form = ReviewForm()

    context = {
        'form': form,
        'car': car
    }
    return render(request, 'inventory/add_review.html', context)