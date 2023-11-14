from django import forms


class EventsForm(forms.Form):
    title = forms.CharField(
        required=True,
        label="Title",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "Enter a title"})
    )
    venue = forms.CharField(
        required=True,
        label="Venue",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "input"})
    )
    max_attendees = forms.IntegerField(
        max_value=1000,
        min_value=2,
        required=True,
        label="Attendees Count",
        widget=forms.NumberInput(attrs={"class": "input"})
    )
    event_type = forms.CharField(
        choices=[('remote', 'remote'), ('offline', 'offline')],
        label='Event Type',
        widget=forms.Select(attrs={'class': 'input'})
    )
    start_date = forms.DateField(
        label="Start Date",
        widget=forms.DateInput(attrs={"class": "input"}))
    end_date = forms.DateField(
        label="End Date", widget=forms.DateInput(attrs={"class": "input"}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "input"}))
