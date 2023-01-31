from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='restaurant-home'),  # Home url
    path('booking/', views.ReservationCreate.as_view(),  # Booking url
         name='restaurant-booking'),
    path('<pk>/', views.ReservationDetailView.as_view(),  # Detail url
         name='restaurant-detail'),
    path('update/<int:pk>/', views.ReservationUpdate.as_view(),  # Update url
         name='restaurant-update'),
]
