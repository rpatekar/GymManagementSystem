from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import Paymenthistory



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('package','register','bookingnumber', 'status')


class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount (INR)', min_value=0.01)

