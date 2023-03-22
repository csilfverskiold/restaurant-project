from django.urls import path
from . import views

urlpatterns = [
    # Home url
    path('', views.HomeView.as_view(), name='home'),
    # Booking url
    path('booking/', views.ReservationCreate.as_view(),
         name='restaurant-booking'),
    # List url
    path('booking/list/', views.ReservationListView.as_view(),
         name='restaurant-list'),
    # Detail url
    path('booking/<pk>/', views.ReservationDetailView.as_view(),
         name='restaurant-detail'),
    # Update url
    path('<pk>/update', views.ReservationUpdateView.as_view(),
         name='restaurant-update'),
    # Delete url
    path('<pk>/delete/', views.ReservationDeleteView.as_view(),
         name='restaurant-delete'),
]
