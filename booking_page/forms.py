from django import forms
from .models import Appointments

class BookingForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['treatment', 'day', 'time']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(pk=user.pk),
                initial=user,
                widget=forms.HiddenInput()
            )
        
        self.fields['day'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['time'].widget = forms.Select(choices=self.fields['time'].choices)

    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get('day')
        time = cleaned_data.get('time')

        if day and time and Appointments.objects.filter(day=day, time=time).exists():
            self.add_error('time', 'We are sorry, this date and time is already booked.')

        return cleaned_data
