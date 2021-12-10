from io import IOBase
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import CharityAddress, Profile
from .forms import ProfileForm, CharityAddressForm


@login_required
def profile(request, user):
    """ View to render users profile """
    profile = Profile.objects.filter(user=request.user)
    address = CharityAddress.objects.filter(user=request.user)
    user = request.user
    context = {
        'profile': profile,
        'address': address,
        'user': user
    }
    return render(request, 'profiles/profile.html', context)


def edit_profile(request, user):
    """ View to render edit profile and allow users to update profile """
    global profile
    try:
        profile = get_object_or_404(Profile, user=request.user)
    except:
        Profile.objects.create(
            user=request.user, name='',
            organisation_name='', type='donor')

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Profile information updated!')
            return redirect(reverse('profile', args=[user]))
        else:
            messages.error(
                request,
                'ERROR: Profile update failed. Please try again.')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
    }
    
    return render(request, 'profiles/edit_profile.html', context)


def edit_address(request, user):
    """ View to render edit address and allow users to update address"""
    if request.method == 'POST':
        form = CharityAddressForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Charity address updated!')
        else:
            messages.error(
                request,
                'ERROR: Profile update failed. Please try again.')

    else:
        form = CharityAddressForm()

    context = {
        'form': form,
        'user': user
    }
    return render(request, 'profiles/edit_contact_address.html', context)