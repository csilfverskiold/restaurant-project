from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Code content inspired by and altered for use in this project:
# https://learndjango.com/tutorials/django-signup-tutorial


# This class renders view to create an account
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
