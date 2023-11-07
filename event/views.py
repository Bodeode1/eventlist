from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q, Count
from django.utils import timezone

# Woprking with forms.
from .forms import EventForm
# Import Models
from .models import Event, Attendee

def index_handler(request):
    query = request.GET.get('query', '')
    events = []
    if query:
        events = Event.objects.filter(title__icontains=query) | Event.objects.filter(description__icontains=query)
    else:
        events = Event.objects.order_by("title")[:2]
    context = {
        "events" : events,
        "user" : request.user
    }

    return render(request, 'events/index.html', context)


def display_signup_form(request):
    return render(request, 'events/signup.html')


def process_signup_form(request):
    try:

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirmpassword"]

        if password != confirm_password:
            messages.success(request, "Password is not equal")
            return redirect("events:events_signup")

        query = Q(username=username) | Q(email=email)
        is_user = User.objects.filter(query)
        if(is_user):
            messages.success(request, "Error, the email you provided is taken")
            return redirect("events:events_signup")
        User.objects.create_user(
            username = username,
            email=email,
            password=password
        )
        messages.success(request, "Your account was created successfully, return to the login")
        return redirect("events:events_login")
    except KeyError as error:
        messages.success(request, "There was an error with your registration, fill the form again correctly")
        return redirect("events:events_signup")


def display_login_form(request):
    return render(request, 'events/login.html')


def authenticate_user(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user, backend=None)
            return redirect("events:user_dashboard")
        else:
            messages.success(request, "Sorry the details you provided are not valid")
            return redirect("events:events_login")
    except KeyError as error:
        messages.success(request, "Sorry, the details you provided are not valid")
        return redirect("events:events_login")


def handle_logout(request):
    logout(request)
    return redirect("events:events_login")


@login_required
def show_dashboard(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    context = {
        'username': user.username,
        'form': EventsForm()
    }
        









