import datetime
from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A model to handle the user profile.
    Handling order history and delivery information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=254, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    paid_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def set_paid_until(self, date_or_timestamp):
        # the input date is a integer
        if isinstance(date_or_timestamp, int):
            paid_until = date.fromtimestamp(date_or_timestamp)
        # the input date is a string
        elif isinstance(date_or_timestamp, str):
            paid_until = date.fromtimestamp(date_or_timestamp)
        else:
            paid_until = date_or_timestamp

        self.paid_until = paid_until
        self.save()

    def has_payed(self, current_date=datetime.date.today()):
        if self.paid_until is None:
            return False
        else:
            return current_date < self.paid_until


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # If user already exist, just save user profile
    instance.userprofile.save()
