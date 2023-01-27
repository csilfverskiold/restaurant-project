from django.shortcuts import render
from django.http import HttpResponse


# This function handles the traffic from the restaurant home page
def home(request):
    return HttpResponse('<h1>Restaurant Home</h1>')


# This function handles the traffic from the restaurant booking page
def booking(request):
    return HttpResponse('<h1>Restaurant Booking</h1>')
