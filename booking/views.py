from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Reservation
from django.contrib.auth.mixins import LoginRequiredMixin


# This class handles the traffic from the restaurant home page
class HomeView(generic.ListView):
    model = Reservation
    template_name = 'booking/index.html'


# This class renders view to create a reservation
class ReservationCreate(LoginRequiredMixin, generic.CreateView):
    model = Reservation
    template_name = 'booking/reservation_form.html'
    fields = (['guest', 'day', 'time', 'first_name', 'last_name', 'email'])

    def get_success_url(self):
        return reverse('restaurant-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        reservation = form.save(commit=False)
        reservation.user = self.request.user
        reservation.save()
        return super().form_valid(form)


# This class renders details of a reservation
class ReservationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reservation
    template_name = 'booking/reservation_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReservationDetailView,
                        self).get_context_data(*args, **kwargs)
        context["category"] = "MISC"
        return context
    # "By default DetailView will only display fields of a table.
    # If one wants to modify this context data before sending it
    # to template or add some extra field, context data can be overridden."


# This class renders a list of reservations
class ReservationListView(LoginRequiredMixin, generic.ListView):
    model = Reservation
    template_name = 'booking/reservation_list.html'

    def get_queryset(self):
        logged_user = self.request.user
        return Reservation.objects.filter(user=logged_user)


# This class renders update of a reservation
class ReservationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Reservation
    template_name = 'booking/reservation_update.html'
    fields = (['guest', 'day', 'time', 'first_name', 'last_name'])
    success_url = "/"


# This class renders delete of a reservation
class ReservationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Reservation
    success_url = "/"
    template_name = "booking/reservation_confirm_delete.html"
