from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    fields = (
        'user',
        'default_full_name',
        'default_email',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_postcode',
        'default_county',
        'default_country',
    )

    list_display = (
        'user',
        'default_full_name',
        'default_email',
    )


admin.site.register(UserProfile, UserProfileAdmin)
