from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


import cloudinary
import cloudinary.uploader
import cloudinary.api
from .models import Gift
from profiles.models import Profile
from .forms import GiftForm


def gifts(request):
    """ View to render gifts template """

    show_gifts = Gift.objects.all()
    show_profile = Profile.objects.all()

    template = 'gifts/gifts.html'
    context = {
        'show_gifts': show_gifts,
        'show_profile': show_profile,
    }

    return render(request, template, context)


@login_required
def add_gift(request, user):
    """ View to add new gifts"""
    verified_profile = Profile.objects.filter(user=request.user, verified=True)

    if not verified_profile:
        messages.error(request, 'Functionality available to the verified users only.')
        return redirect(reverse('gifts'))
    
    if request.method == 'POST':
        add_gift_form = GiftForm(request.POST, request.FILES)
        if add_gift_form.is_valid():
            add_gift_form = add_gift_form.save(commit=False)
            add_gift_form.user = request.user
            add_gift_form.save()
            messages.success(request, 'Successfully added a new gift!')
            return redirect('gifts')
        else:
            messages.error(request, 'Failed to add a new gift. Please ensure the form is valid.')

    else:
        add_gift_form = GiftForm()

    template = 'gifts/add-gifts.html'
    context = {
        'add_gift_form': add_gift_form,
        "user": user,
    }
    return render(request, template, context)