from creditapp.models import *
from django import forms

class Addcard(forms.ModelForm):
    class Meta:
        model=Card
        exclude = ['id','user']
        widgets={
            ' friendly_name':forms.TextInput(attrs={'class':'form-control','placeholder':'friendly name'}),
            'name_on_card':forms.TextInput(attrs={'class':'form-control','placeholder':'card name'}),
            'expiry_date':forms.DateInput(attrs={'class':'form-control','placeholder':'expirydate'}),
            'typec':forms.TextInput(attrs={'class':'form-control','placeholder':'type'}),
            'cvv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cvv'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cardnumber'})
        }



class Loginform(forms.Form):
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter first name'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter first name'})
    )