from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from .models import Reservation


# This function handles the traffic from the restaurant home page
def home(request):
    return HttpResponse('<h1>Restaurant Home</h1>')


class ReservationCreate(CreateView):  # Renders view to create a reservation
    model = Reservation
    fields = (['guest', 'day', 'time',
               'content', 'first_name', 'last_name', 'email'])

    def get_success_url(self):
        return reverse('restaurant-detail', kwargs={'pk': self.object.pk})


class ReservationDetailView(DetailView):  # Renders details of a reservation
    model = Reservation

    def get_context_data(self, *args, **kwargs):
        context = super(ReservationDetailView,
                        self).get_context_data(*args, **kwargs)
        context["category"] = "MISC"
        return context
    # "By default DetailView will only display fields of a table.
    # If one wants to modify this context data before sending it
    # to template or add some extra field, context data can be overridden."


class ReservationUpdateView(UpdateView):  # Renders update of a reservation
    model = Reservation
    fields = (['guest', 'day', 'time',
               'content', 'first_name', 'last_name'])
    success_url = "/"
