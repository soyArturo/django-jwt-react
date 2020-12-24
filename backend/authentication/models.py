from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(blank=True, max_length=20)
    fav_color = models.CharField(blank=True, max_length=120)
