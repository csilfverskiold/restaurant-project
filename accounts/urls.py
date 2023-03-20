from django.urls import path
from .views import SignUpView


urlpatterns = [
    # Signup url
    path("signup/", SignUpView.as_view(), name="signup"),
]
