from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Home url
    path('booking/', views.ReservationCreate.as_view(),  # Booking url
         name='restaurant-booking'),
    path('booking/<pk>/', views.ReservationDetailView.as_view(),  # Detail url
         name='restaurant-detail'),
    path('booking/<pk>/update', views.ReservationUpdateView.as_view(),  # Update url
         name='restaurant-update'),
]
