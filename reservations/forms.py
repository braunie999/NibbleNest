from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_datetime', 'number_of_guests', 'table']
    widgets = {
        'booking_datetime': forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }
        ),
        'table': forms.Select(attrs={'class': 'form-control'}),
        'number_of_guests': forms.NumberInput(
            attrs={
                'min': 1,
                'class': 'form-control'
            }
        ),
    }


def clean_booking_datetime(self):
    booking_datetime = self.cleaned_data.get('booking_datetime')
    if booking_datetime < timezone.now():
        raise forms.ValidationError(
            "The booking date and time cannot be in the past.")
    return booking_datetime
