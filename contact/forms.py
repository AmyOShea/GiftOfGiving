from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form for Contact model """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'comments']