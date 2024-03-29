from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q, Count
from django.utils import timezone

# Woprking with forms.
from .forms import EventsForm
# Import Models
from .models import Event, Attendee

# Handler for the index page
def index_handler(request):
    # Get the query parameter from the request
    query = request.GET.get('query', '')
    events = []

    # Filter events based on query or get first two events if no query provided
    if query:
        events = Event.objects.filter(title__icontains=query) | Event.objects.filter(
            description__icontains=query)
    else:
        events = Event.objects.order_by("start_date")[:12]

    # Define context data with events and user information
    context = {
        "events": events,
        "user": request.user
    }

    return render(request, 'events/index.html', context)

# Display signup form
def display_signup_form(request):
    return render(request, 'events/signup.html')

# Processes user signup form data
def process_signup_form(request):
    try:
        # Extract user details from the POST request
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirmpassword"]

        # Validate password match
        if password != confirm_password:
            messages.success(request, "Password is not equal")
            return redirect("events:events_signup")

        # Check if username or email already exists
        query = Q(username=username) | Q(email=email)
        is_user = User.objects.filter(query)
        if (is_user):
            messages.success(request, "Error, the email you provided is taken")
            return redirect("events:events_signup")

        # Create a new user with provided details
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Display success message and redirect to login page
        messages.success(
            request, "Your account was created successfully, return to the login")
        return redirect("events:events_login")
    except KeyError as error:
        messages.success(
            request, "There was an error with your registration, fill the form again correctly")
        return redirect("events:events_signup")

# Display Login form
def display_login_form(request):
    return render(request, 'events/login.html')

# Authenticate user based on login credentials
def authenticate_user(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user, backend=None)
            return redirect("events:user_dashboard")
        else:
            messages.success(
                request, "Sorry the details you provided are not valid")
            return redirect("events:events_login")
    except KeyError as error:
        messages.success(
            request, "Sorry, the details you provided are not valid")
        return redirect("events:events_login")

# Handle user logout
def handle_logout(request):
    logout(request)
    return redirect("events:events_login")

# Show user dashboard with event statistics
@login_required
def show_dashboard(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    total_events_created = Event.objects.filter(creator=user).count()
    total_events_completed = Event.objects.filter(
        creator=user, status=True).count()
    total_attendees_for_your_event = Attendee.objects.filter(
        event__creator=user).count()
    print(total_attendees_for_your_event)
    context = {
        'username': user.username,
        "total_events_created": total_events_created,
        "total_events_completed": total_events_completed,
        "total_attendees": total_attendees_for_your_event
    }
    return render(request, "events/dashboard.html", context)


def handle_logout(request):
    logout(request)
    return redirect("events:events_login")

# Displays the add event form


@login_required
def add_event_view(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    context = {
        'username': user.username,
        'form': EventsForm(),
    }
    return render(request, "events/add-event.html", context)

# Handle adding an event from the form data
@login_required
def handle_add_event(request):
    try:
        # Handles creation of event. 
        form = EventsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            venue = form.cleaned_data['venue']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            max_attendees = form.cleaned_data["max_attendees"]
            event_type = form.cleaned_data["event_type"]
            user_id = request.user.id
            user = User.objects.get(pk=user_id)

            Event.objects.create(
                title=title,
                description=description,
                venue=venue,
                start_date=start_date,
                end_date=end_date,
                max_attendees=max_attendees,
                event_type=event_type,
                creator=user
            )

            messages.success(request, 'Your event was created successfully')
            return redirect("events:add_event_view")
        else:
            messages.success(
                request, 'Fill the form correctly with right data')
            return redirect("events:add_event_view")
    except KeyError as error:
        messages.success(request, "Fill the form correctly")
        return redirect("events:add_event_view")

# Shows events associated with the logged-in user. Then annotates each event with the count of attendees.
@login_required
def show_user_events(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)

    events = Event.objects.filter(creator=user).annotate(
        attendee_count=Count('attendee'))

    context = {
        "events": events,
        'username': user.username,
    }
    return render(request, "events/event-list.html", context)


#  Retrieves details of a single event based on the provided event ID and calculates the number of attendees and remaining tickets.
@login_required
def get_single_event(request, id):
    try:
        event = Event.objects.get(pk=id)
        attendees_count = Attendee.objects.filter(event=event).count()
        ticket_remaining = event.max_attendees - attendees_count
        context = {
            "event": event,
            "attendees_count": attendees_count,
            "ticket_remaining": ticket_remaining
        }
        return render(request, "events/event-detail.html", context)
    except Event.DoesNotExist:
        raise Http404("You do not have an event with that id")

# Delete an event by it's id

# Handles the deletion of a single event. It verifies if the event exists and if the logged-in user is the creator of that event before deleting 
@login_required
def delete_single_event(request, id):
    try:
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        event = Event.objects.get(pk=id, creator=user)
    except Event.DoesNotExist:
        raise Http404("You do not have an event with that id")

    Event.objects.filter(pk=id).delete()
    return render(request, "events/event-delete-success.html")

# Get ticket for an event


def purchase_event(request, id):
    # Fetch the Event object based on the provided ID
    event = Event.objects.get(pk=id)

    # Calculate the count of attendees for this event
    attendees_count = Attendee.objects.filter(event=event).count()

    # Calculate the remaining tickets available for purchase
    ticket_remaining = event.max_attendees - attendees_count

    # Create a context dictionary containing event details and ticket availability
    context = {
        "event": event,
        "ticket_remaining": ticket_remaining
    }
    return render(request, "events/event-purchase.html", context)

# Get ticket for an event


def process_event_checkout(request, id):
    try:
        name = request.POST["name"]
        email = request.POST["email"]
        event = Event.objects.get(pk=id)
        context = {
            "event": event
        }
        user = User.objects.get(pk=event.creator.id)

        attendees_count = Attendee.objects.filter(event=event).count()
        ticket_remaining = event.max_attendees - attendees_count

        if ticket_remaining == 0:
            messages.success(
                request, "Sorry, there is no more ticket available for purchase")
            return render(request, "events/event-purchase.html", context)
        # checks if the intending attendee is the creator of the event
        if user and user.email == email:
            messages.success(
                request, "You cannot register as an attendeefor an event you created")
            return render(request, "events/event-purchase.html", context)

        # Checks if the user has registered for the event before
        is_attendee = Attendee.objects.get(email=email, event=event)
        if is_attendee:
            messages.success(
                request, "You cannot register twice for a single event")
            return render(request, "events/event-purchase.html", context)
    except Attendee.DoesNotExist:
        Attendee.objects.create(
            email=email,
            name=name,
            event=event
        )
        messages.success(request, "You successfully bought the ticket")
        return render(request, "events/event-purchase.html", context)
    except Event.DoesNotExist:
        raise Http404("You do not have an event with that id")
    except KeyError as error:
        messages.success(request, 'Fill the form correctly with right data')
        return render(request, "events/event-purchase.html", context)


@login_required
def edit_event(request, id):
    try:

        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        event = Event.objects.get(pk=id, creator=user)

        # Format the date as a string in ISO format (YYYY-MM-DD)
        start_date = event.start_date.strftime('%Y-%m-%d')
        end_date = event.end_date.strftime('%Y-%m-%d')
        context = {
            "event": event,
            "start_date": start_date,
            "end_date": end_date,
            'username': user.username,
        }
        return render(request, "events/edit-event.html", context)

    except Event.DoesNotExist:
        raise Http404("You do not have an event with that id")

# Hadnles the editing and saving of an event.
# Retrieves event details, validate the date range, and update the event.
@login_required
def save_edit_event(request, id):
    try:

        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        event = Event.objects.get(pk=id, creator=user)
        context = {
            "event": event,
            "start_date": event.start_date.strftime('%Y-%m-%d'),
            "end_date": event.end_date.strftime('%Y-%m-%d')
        }
        title = request.POST['title']
        description = request.POST['description']
        venue = request.POST['venue']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        max_attendees = request.POST["max_attendees"]
        status = request.POST['status']
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        print(start_date, end_date)
        if start_date > end_date:
            messages.success(
                request, "Event start date cannot be greater than end date")
            return render(request, "events/edit-event.html", context)
        event.title = title
        event.venue = venue
        event.description = description
        event.start_date = start_date
        event.end_date = end_date
        event.max_attendees = max_attendees
        event.status = status

        event.save()

        messages.success(request, "You have successfully updated your event")
        return render(request, "events/edit-event.html", context)
    except Event.DoesNotExist:
        raise Http404("You do not have an event with that id")
    except Exception as error:
        print(error)
        messages.success(request, "An error occured, try again")
        return render(request, "events/edit-event.html", context)
