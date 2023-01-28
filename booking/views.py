from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Reservation


# This function handles the traffic from the restaurant home page
def home(request):
    return HttpResponse('<h1>Restaurant Home</h1>')


class ReservationCreate(CreateView):  # Renders Reservation to create view
    model = Reservation
    fields = (['service', 'guest', 'day', 'time',
               'content', 'first_name', 'last_name', 'email'])
