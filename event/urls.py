from django.urls import path
from . import views

app_name = "events"
urlpatterns = {
    path("", views.index_handler, name="events_index"),
    path("sign-up/", views.display_signup_form, name="events_signup"),
    path("login/", views.display_login_form, name="events_login"),
    path("logout/", views.handle_logout, name="events_logout"),
    path("process-signup/", views.process_signup_form, name="process_signup"),
    path("process-login/", views.authenticate_user, name="process_login"),
    path("checkout/<int:id>", views.process_event_checkout, name="checkout"),
    path("get-event/<int:id>", views.purchase_event, name="events_index"),
    
}