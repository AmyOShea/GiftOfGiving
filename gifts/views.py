from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


import cloudinary
import cloudinary.uploader
import cloudinary.api
from .models import Gift
from profiles.models import CharityAddress, Profile
from .forms import GiftForm


def gifts(request):
    """ View to render gifts template """

    show_gifts = Gift.objects.all()
    
    template = 'gifts/gifts.html'
    context = {
        'show_gifts': show_gifts,
    }

    return render(request, template, context)


@login_required
def add_gift(request, user):
    """ View to add new gifts"""

    verified_profile = Profile.objects.filter(user=request.user, verified=True)

    if not verified_profile:
        messages.error(request, (
            'Functionality available to the verified users only.' +
            'Please ensure profile is updated and email verification documents.')
        )
        return redirect(reverse('gifts'))

    org_name = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        add_gift_form = GiftForm(request.POST, request.FILES)
        if add_gift_form.is_valid():
            add_gift_form = add_gift_form.save(commit=False)
            add_gift_form.organisation_name = org_name.organisation_name
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
    }
    return render(request, template, context)


@login_required
def edit_gift(request, id):
    """ View to edit new gifts"""
    try:
        gift = get_object_or_404(Gift, id=id)
        profile = Profile.objects.get(user=request.user)
    except:
        messages.error(request, (
            'Error. Gift or profile not found.')
        )
        return redirect(reverse('gifts'))
    
    profile = Profile.objects.get(user=request.user)  
    if not profile.organisation_name == gift.organisation_name:
        messages.error(request, (
            'You do not have permission to edit this gift')
        )
        return redirect(reverse('gifts'))

    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES, instance=gift)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited gift!')
            return redirect('gifts')
        else:
            messages.error(request, 'Failed to edit gift. Please ensure the form is valid.')

    else:
        form = GiftForm(instance=gift)

    template = 'gifts/edit-gifts.html'
    context = {
        'form': form,
        'gift': gift
    }
    return render(request, template, context)


@login_required
def view_gift(request, user, id):
    """ View to return single gift and allow users to commit to buy """
    try:
        gift = get_object_or_404(Gift, id=id)
    except:
        messages.error(request, 'Something went wrong. Unable to load gift.')
        return redirect('gifts')
    
    gift = get_object_or_404(Gift, id=id)
    address = CharityAddress.objects.get(organisation_name=gift.organisation_name)
    
    profile = Profile.objects.get(organisation_name=gift.organisation_name)
    
    context = {
        'gift': gift,
        'address': address,
        'profile': profile
    }

    if request.method == 'POST':
        form = GiftForm(instance=gift)
        form = form.save(commit=False)
        form.committed_by = request.user
        form.save()
        messages.success(request, 'Thank you for agreeing to purchase this gift.')
        return render(request, 'gifts/view_gift.html', context)

    return render(request, 'gifts/view_gift.html', context)