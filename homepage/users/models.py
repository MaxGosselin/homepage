from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator 



class User(AbstractUser):
    RCHOICES = (
    ("Yes", "Yes"),
    ("No", "No"),
    )

    recruiter = models.CharField(max_length=3, choices=RCHOICES, default="No")
