from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . forms import UserRegistrationForm


# Create your views here.
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'users/login.html', {"login_form":form})


def register_form(request):	
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been created! You can now able to login')
			return redirect('login')
	form = UserRegistrationForm()
	return render(request, 'users/register_form.html', {'form':form})

def logout_form(request):
    logout(request)
    messages.success(request, "You have successfully logged out.") 
    return redirect('index')