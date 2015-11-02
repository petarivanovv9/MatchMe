from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
	return render(request, "index.html")


def user_login(request):
	return render(request, "login.html")


def user_logout(request):
	pass


def _validate_register(username, email, password, password2):
	pass


def user_register(request):
	return render(request, "register.html")	