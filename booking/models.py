from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Import this later when needed- from cloudinary.models import CloudinaryField


TIME_CHOICES = (
    ('5 PM', '5 PM'),
    ('5:30 PM', '5:30 PM'),
    ('6 PM', '6 PM'),
    ('6:30 PM', '6:30 PM'),
    ('7 PM', '7 PM'),
    ('7:30 PM', '7:30 PM'),
    ('8 PM', '8 PM'),
    ('8:30 PM', '8:30 PM'),
    ('9 PM', '9 PM'),
    ('9:30 PM', '9:30 PM'),
)

GUEST_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


# Model for making reservations, CRUD functionality included.


class Reservation (models.Model):
    guest = models.CharField(max_length=10, choices=GUEST_CHOICES)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    content = models.TextField(max_length=500, default="", blank=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)

    def __str__(self):
        return f"""Name: {self.first_name} {self.last_name}
         | Guest: {self.guest} | Day: {self.day} | Time: {self.time}"""
