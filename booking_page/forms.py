from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking


class BookingForm(forms.ModelForm):
    """A form to create a booking"""
    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=True, label="Last Name")
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

        self.fields['treatment'].label = "Treatment"
        self.fields['day'].label = "Date"
        self.fields['day'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['day'].required = True

    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get('day')
        time = cleaned_data.get('time')

        # Check if a booking with the same day and time already exists
        if day and time and Booking.objects.filter(day=day, time=time).exists():
            self.add_error('time', 'This date and time is already booked.')

        return cleaned_data

    class Meta:
        model = Booking
        fields = ['treatment', 'day', 'time']