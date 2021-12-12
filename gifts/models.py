from django.db import models
import uuid
import cloudinary
import cloudinary.uploader
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField


AGE_RANGE_CHOICES = (
    ('0-1', '0-1'),
    ('1-3', '1-3'),
    ('3-5', '3-5'),
    ('6-7', '6-7'),
    ('7-10', '7-10'),
    ('10-13', '10-13'),
    ('13-16', '13-16')
)

class Gift(models.Model):
    """
    A model to create a profile for a user
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    organisation_name = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=1550, null=False, blank=False)
    estimated_price = models.DecimalField(decimal_places=2, default=0, max_digits=6)
    age_range = models.CharField(max_length=25,
                                    choices=AGE_RANGE_CHOICES,
                                    null=False, blank=False)
    image = models.ImageField(upload_to='gift_images/', blank=True)
    needed = models.BooleanField(default=True)
    committed = models.BooleanField(default=False)
    committed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.description
