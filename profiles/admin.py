from django.contrib import admin
from .models import Profile, CharityAddress


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'organisation_name',
        'type',
        'verified'
    )


class CharityAddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'address_line_one',
        'address_line_two',
        'address_line_three',
        'county',
        'country',
        'postcode'
    )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(CharityAddress, CharityAddressAdmin)