from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, db_index=True)
    description = models.TextField()
    venue = models.CharField(max_length=100)
    tags = models.CharField(max_length=50, null=True)
    status = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    event_type = models.CharField(max_length=20)
    gate_fee = models.DecimalField(max_digits=10, decimal_places=2)
    max_attendees = models.PositiveIntegerField()
    current_attendees_count = models.PositiveIntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


# class Ticket(models.Model):
#   title = models.CharField(max_length=50)
#   amount = models.DecimalField(default=0, max_digits=10)
#   initial_quantity = models.PositiveIntegerField()
#   quantity_available = models.PositiveIntegerField()
#    event = models.ForeignKey(Event, on_delete=models.CASCADE)

#   def __str__(self) -> str:
#       return self.title


class Attendee(models.Model):
    email = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=100)
    ticket_quantity = models.PositiveIntegerField(default=1)
    amount_paid = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    

    





