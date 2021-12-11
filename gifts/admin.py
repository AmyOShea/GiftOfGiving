from django.contrib import admin
from .models import Gift

# Register your models here.
class GiftAdmin(admin.ModelAdmin):
    list_display = (
        'organisation_name',
        'description',
        'estimated_price',
        'age_range',
        'needed',
        'committed',
        'committed_by',
        'received'
    )


admin.site.register(Gift, GiftAdmin)