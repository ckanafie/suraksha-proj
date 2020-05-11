from django.contrib.auth.forms import UsserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Cust, Drvr

class CustSignUpForm(UserCreationForm):
    class Meta:
        model = Cust
        fields = ('username','first_name','last_name','email','password1','password2','gender','dob','mobile','address')

class DrvrSignUpForm(UserCreationForm):
    class Meta:
        model = Drvr
        fields = ('username','first_name','last_name','email','password1','password2','gender','dob','mobile','address')
