from django.conf import settings
from django.db import models
from django.utils import timezone

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Cust(models.Model):
    cust_id = models.IntegerField()
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=gender_choices)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drvr(models.Model):
    cab_id = models.IntegerField()
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=gender_choices)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class book(models.Model):
    cust_id = models.ForeignKey(Cust, on_delete=models.CASCADE)
    cab_id = models.ForeignKey(Drvr, on_delete=models.CASCADE)
    src = models.CharField(max_length=100)
    dst = models.CharField(max_length=100)
