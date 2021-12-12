from io import IOBase
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import CharityAddress, Profile
from gifts.models import Gift
from .forms import ProfileForm, CharityAddressForm


@login_required
def profile(request, user):
    """View to render users profile"""
    # Get object or create empty one
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={"name": "", "organisation_name": "", "type": "donor"},
    )
    # Get object or create empty one
    address, created = CharityAddress.objects.get_or_create(
        user=request.user,
        defaults={
            "county": "",
            "country": "",
            "address_line_one": "",
            "organisation_name": "",
        },
    )
            
    user = request.user
    context = {"profile": profile, "address": address, "user": user}

    try:
        gifts = Gift.objects.filter(committed_by=request.user)
        charity_gifts = Gift.objects.filter(organisation_name=profile.organisation_name, needed=True)
        context = {"profile": profile, "address": address, "user": user, 'gifts': gifts, 'charity_gifts': charity_gifts}
    except:
        return render(request, "profiles/profile.html", context)

    return render(request, "profiles/profile.html", context)


@login_required
def edit_profile(request, user):
    """View to render edit profile and allow users to update profile"""
    user=request.user
    # Get object or create empty one
    profile, created = Profile.objects.get_or_create(
        user=user,
        defaults={"name": "", "organisation_name": "", "type": "donor"},
    )

    # Get object or create empty one
    address, created = CharityAddress.objects.get_or_create(
        user=user,
        defaults={
            "county": "",
            "country": "",
            "address_line_one": "",
            "organisation_name": "",
        },
    )

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            # Add user before commit
            form = form.save(commit=False)
            form.user = user
            form.save()
            # Update Charity Address table with org name
            org_name = CharityAddressForm(instance=address)
            org_name = org_name.save(commit=False)
            org_name.organisation_name = form.organisation_name
            org_name.save()
            messages.success(request, "Profile information updated!")
            return redirect(reverse("profile", args=[user]))
        else:
            messages.error(request, "ERROR: Profile update failed. Please try again.")
    else:
        form = ProfileForm(instance=profile)

    context = {"form": form, "user": user}

    return render(request, "profiles/edit_profile.html", context)


@login_required
def edit_address(request, user):
    """View to render edit address and allow users to update address"""
    user=request.user
    # Get object or create empty one
    address, created = CharityAddress.objects.get_or_create(
        user=user,
        defaults={
            "county": "",
            "country": "",
            "address_line_one": "",
            "organisation_name": "",
        },
    )

    if request.method == "POST":
        form = CharityAddressForm(request.POST, instance=address)
        if form.is_valid():
            # Add user before submitting form
            form = form.save(commit=False)
            form.user = user
            form.save()
            messages.success(request, "Charity address updated!")
            return redirect(reverse("profile", args=[user]))
        else:
            messages.error(request, "ERROR: Profile update failed. Please try again.")

    else:
        form = CharityAddressForm(instance=address)

    context = {"form": form, "user": user}
    return render(request, "profiles/edit_contact_address.html", context)
