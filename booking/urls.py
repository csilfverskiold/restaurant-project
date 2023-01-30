from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='restaurant-home'),  # Home url
    path('booking/', views.ReservationCreate.as_view(),
         name='restaurant-booking'),  # Booking url
    path('list/', views.ReservationList.as_view(),
         name='restaurant-list'),  # List url
    path('update/', views.ReservationUpdate.as_view(),
         name='restaurant-update'),  # Update url
]
