from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'comments',
    )


admin.site.register(Contact, ContactAdmin)