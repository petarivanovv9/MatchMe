from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "index.html")


def user_login(request):
    if request.user.is_authenticated():
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")
        else:
            return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("index")


def _validate_register(username, email, password, password2):
    if username is None or username.strip() == "":
        return False

    if email is None or email.strip() == "":
        return False

    if password is None or password.strip() == "" or password != password2:
        return False

    return True


def user_register(request):
	if request.user.is_authenticated():
		return redirect("index")
	else:
		if request.method == "POST":
			username = request.POST.get("username")
			email = request.POST.get("email")
			password_1 = request.POST.get("password")
			password_2 = request.POST.get("password2")
			
			if not _validate_register(username, email, password, password2):
                return redirect("register")

            user = User.objects.create_user(username, email, password)

            if user is not None:
            	user = authenticate(username=username, password=password)
            	login(request, user)
            	return redirect("index")
            else:
            	return render(request, "register.html")

		else:
			return render(request, "register.html")