from django import forms
from .models import Appointments

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['treatment', 'day', 'time']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['day'].widget.attrs['type'] = 'date'
