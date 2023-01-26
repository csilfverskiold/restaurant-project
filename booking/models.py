from django.db import models
from django.contrib.auth.models import User
# Import this later when needed- from cloudinary.models import CloudinaryField


class Reservation (models.Model):
    name = models.CharField(max_length=200)
