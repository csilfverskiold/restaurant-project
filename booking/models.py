from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Code content inspired by and altered for use in this project:
# https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78

TIME_CHOICES = (
    ('5:00 PM', '5:00 PM'),
    ('5:30 PM', '5:30 PM'),
    ('6:00 PM', '6:00 PM'),
    ('6:30 PM', '6:30 PM'),
    ('7:00 PM', '7:00 PM'),
    ('7:30 PM', '7:30 PM'),
    ('8:00 PM', '8:00 PM'),
    ('8:30 PM', '8:30 PM'),
    ('9:00 PM', '9:00 PM'),
    ('9:30 PM', '9:30 PM'),
)

GUEST_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


# Model for making reservations, CRUD functionality included


class Reservation (models.Model):
    guest = models.CharField(max_length=10, choices=GUEST_CHOICES)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)

    def __str__(self):  # Returns a string representation of the object
        return f"""Name: {self.first_name} {self.last_name}
         | Guest: {self.guest} | Day: {self.day} | Time: {self.time}"""
