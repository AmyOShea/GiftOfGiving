from django.contrib import admin
from .models import Gift, Donation


# Register your models here.
class GiftAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'description',
        'estimated_price',
        'age_range',
        'needed',
        'committed',
        'committed_by',
        'received'
    )

class DonationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'contact_number'
    )

admin.site.register(Gift, GiftAdmin)
admin.site.register(Donation, DonationAdmin)