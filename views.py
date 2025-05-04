from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Ride
from .forms import RideForm

def home(request):
    rides = Ride.objects.filter(status='pending')
    return render(request, 'home.html', {'rides': rides})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def create_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.driver = request.user
            ride.save()
            return redirect('home')
    else:
        form = RideForm()
    return render(request, 'create_ride.html', {'form': form})

@login_required
def accept_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    if ride.status == 'pending':
        ride.passenger = request.user
        ride.status = 'accepted'
        ride.save()
    return redirect('home')
