from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.template import RequestContext
from django.contrib import messages
from .forms import CustSignUpForm, DrvrSignUpForm
from .models import Cust,Drvr

def home_pg(request):
    return render(request, 'suraksha/home_pg.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,('you ave been successfully Logged Out'))
    return redirect('home_pg')

def login_cust(request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('you have been logged in'))
			return redirect('cust_home')
		else:
			messages.success(request,('Error login in log in with valid username..'))
			return redirect('login')
	else:
		return render(request,'login_cust.html',{})

def reg_cust(request):
    if request.method == 'POST':
        form = CustSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,('You have been successfully registered'))
            return redirect('cust_home')
    else:
        form = CustSignUpForm()
    context={'form':form}
    return render(request,'reg_cust.html',context)

def login_drvr(request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('you have been logged in'))
			return redirect('drvr_home')
		else:
			messages.success(request,('Error login in log in with valid username..'))
			return redirect('login')
	else:
		return render(request,'login_drvr.html',{})

def reg_drvr(request):
    if request.method == 'POST':
        form = DrvrSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,('You have been successfully registered'))
            return redirect('drvr_home')
    else:
        form = DrvrSignUpForm()
    context={'form':form}
    return render(request,'reg_drvr.html',context)
