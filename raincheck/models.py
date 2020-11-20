from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Location(models.Model):
    region = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    continent = models.CharField(max_length=20, null=True, blank=True)
    last_rained = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return ', '.join([self.region, self.country])


class Plant(models.Model):
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    reference = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('plant-detail', args=[str(self.id)])


class CustomerPlant(models.Model):  # join table gives more flexibility than m2m field
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('customerplant-detail', args=[str(self.id)])


class Email(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_emails")
    datetime = models.DateTimeField(auto_now=True)
