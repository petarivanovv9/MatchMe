from django.shortcuts import render, redirect

from django.shortcuts import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import Event, EventUser
from .models import UserProfile, City

# Create your views here.


def index(request):
    events = Event.objects.all()
    user_id = request.user.id
    user_events = []
    for elem in EventUser.objects.filter(user_id=user_id):
        user_events.append(Event.objects.get(id=elem.event.id))

    return render(request, "index.html", locals())


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
            password = request.POST.get("password")
            password_2 = request.POST.get("password2")

            if not _validate_register(username, email, password, password_2):
                return redirect("register")

            user = User.objects.create_user(username, email, password)
            UserProfile.objects.create(user=user)

            if user is not None:
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("index")
            else:
                return render(request, "register.html")

        else:
            return render(request, "register.html")


@login_required
def view_event(request, event_id):
    current_event = Event.objects.get(pk=event_id)

    bam = EventUser.objects.filter(event_id=event_id, user_id=request.user.id)
    has_attended = True
    if not bam:
        has_attended = False

    return render(request, "event.html", locals())


@login_required
def attend_event(request, event_id):
    EventUser(event_id=event_id, user_id=request.user.id).save()

    return redirect("index")


@login_required
def view_profile(request):
    user_id = request.user.id

    user_profile = UserProfile.objects.get(user_id=user_id)

    user_profile_data = {}
    user_profile_data["first_name"] = user_profile.first_name
    user_profile_data["last_name"] = user_profile.last_name
    user_profile_data["city"] = user_profile.city
    user_profile_data["age"] = user_profile.age

    return render(request, "profile.html", locals())


@login_required
def edit_profile(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        print(first_name)

        age = request.POST.get("age")

        city_name = request.POST.get("city")
        city = City.objects.get(name=city_name)

        user_id = request.user.id
        user_profile = UserProfile.objects.get(user_id=user_id)

        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.age = age
        user_profile.city = city
        user_profile.save()

        return redirect(view_profile)
    else:
        cities = City.objects.all()

    return render(request, "edit_profile.html", locals())
