from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("", views.index_handler, name="events_index"),
    path("sign-up/", views.display_signup_form, name="events_signup"),
    path("login/", views.display_login_form, name="events_login"),
    path("logout/", views.handle_logout, name="events_logout"),
    path("process-signup/", views.process_signup_form, name="process_signup"),
    path("process-login/", views.authenticate_user, name="process_login"),
    path("checkout/<int:id>", views.process_event_checkout, name="checkout"),
    path("get-event/<int:id>", views.purchase_event, name="events_index"),
     path("dashboard/", views.show_dashboard, name="user_dashboard"),
    path("dashboard/add-event/", views.add_event_view, name="add_event_view"),
    path("dashboard/process-add-event/", views.handle_add_event, name="process_event"),
    path("dashboard/your-events", views.show_user_events, name="user_events"),
    path("dashboard/create-event/<int:id>/", views.get_single_event, name="single_event"),
    path("dashboard/delete-event/<int:id>/", views.delete_single_event, name="delete_single_event"),
    path("dashboard/edit-event/<int:id>/", views.edit_event, name="edit_event_view"),
    path("dashboard/save-edit-event/<int:id>/", views.save_edit_event, name="save_edit_event")
]