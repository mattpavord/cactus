from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Customer(models.Model):
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plants = models.ManyToManyField("Plant")
    last_emailed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    continent = models.CharField(max_length=20, null=True, blank=True)
    last_rained = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return ', '.join([self.name, self.country])


class Plant(models.Model):
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    reference = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class Email(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sent_emails")
    datetime = models.DateTimeField(auto_now=True)
