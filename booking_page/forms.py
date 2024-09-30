from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking

class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['date'].required = True
        self.fields['time'].required = True
        self.fields['treatment'].required = True

        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if (date and time and
                Booking.objects.filter(date=date, time=time).exists()):
            self.add_error('time', 'We are sorry, this date and time is already booked.')

    class Meta:
        model = Booking
        fields = [
            'first_name', 'last_name', 'email', 'treatment', 'date', 'time',
        ]