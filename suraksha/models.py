from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Cust(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
    dob = models.DateField(blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user.username)

class Drvr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
    dob = models.DateField(blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (self.user.username)

class book(models.Model):
    cust = models.ForeignKey('Cust', on_delete=models.CASCADE)
    drvr = models.ForeignKey('Drvr', on_delete=models.CASCADE)
    src = models.CharField(max_length=100)
    dst = models.CharField(max_length=100)
