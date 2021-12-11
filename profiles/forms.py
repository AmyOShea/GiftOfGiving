from django import forms
from .models import CharityAddress, Profile


class ProfileForm(forms.ModelForm):
    """ Form for Profile model """
    class Meta:
        model = Profile
        fields = ['name', 'organisation_name', 'type']


class CharityAddressForm(forms.ModelForm):
    """ Form for Charity Address model """
    class Meta:
        model = CharityAddress
        fields = [
            'address_line_one',
            'address_line_two',
            'address_line_three',
            'county',
            'country',
            'postcode'
        ]
