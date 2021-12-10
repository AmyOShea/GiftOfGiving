from django.db import models
from django.contrib.auth.models import User


USER_TYPE_CHOICES = (
    ('charity', 'CHARITY'),
    ('donor', 'DONOR')
)


class Profile(models.Model):
    """
    A model to create a profile for a user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,
                             null=False, blank=False)
    organisation_name = models.CharField(max_length=150,
                            null=True, blank=True)
    type = models.CharField(max_length=25,
                                      choices=USER_TYPE_CHOICES,
                                      null=False, blank=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class CharityAddress(models.Model):
    """ 
    A model to create an address for a charity
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organisation_name = models.CharField(max_length=150,
                            null=True, blank=True)
    address_line_one = models.CharField(max_length=150,
                            null=True, blank=True)
    address_line_two = models.CharField(max_length=150,
                            null=True, blank=True)
    address_line_three = models.CharField(max_length=150,
                            null=True, blank=True)
    county = models.CharField(max_length=150,
                            null=False, blank=False)
    country = models.CharField(max_length=150,
                            null=False, blank=False)
    postcode = models.CharField(max_length=150,
                            null=True, blank=True)

    def __str__(self):
        return self.organisation_name