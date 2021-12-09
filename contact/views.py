from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def contact(request):
    """ View to render the contact page"""
    return render(request, 'contact/contact.html')