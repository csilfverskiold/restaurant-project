from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import Reservation


# This function handles the traffic from the restaurant home page
def home(request):
    return HttpResponse('<h1>Restaurant Home</h1> <a href="https://8000-csilfverski-restaurantp-dv4iba0kkur.ws-eu84.gitpod.io/booking/">Reservation</a>')


class ReservationCreate(CreateView):  # Renders Reservation to create view
    model = Reservation
    fields = (['guest', 'day', 'time',
               'content', 'first_name', 'last_name', 'email'])


class ReservationList(generic.ListView):
    model = Reservation


class ReservationUpdate(UpdateView):
    model = Reservation
    fields = (['guest', 'day', 'time',
               'content', 'first_name', 'last_name'])
    template_name_suffix = '_update_form'
