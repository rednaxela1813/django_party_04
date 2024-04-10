from os import name
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class CustomUser(AbstractUser):
    pass


class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation = models.TextField()
    venue = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="organized_parties")

    class Meta:
        verbose_name_plural = "parties"

    def __str__(self):
        return f"{self.party_date} at {self.venue}"
    

class Gift(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    gift = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="gifts")

    def __str__(self):
        return self.gift    
    

class Guest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    attending = models.BooleanField(default=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="guests")

    def __str__(self):
        return self.name
    