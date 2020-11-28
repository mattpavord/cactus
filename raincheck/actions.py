from django.http import HttpResponseRedirect
from django.urls import reverse

from raincheck.models import CustomerPlant


def add_to_garden(request, plant_id):
    if request.user.is_authenticated:
        CustomerPlant.objects.create(customer_id=request.user.id, plant_id=plant_id)
        return HttpResponseRedirect(reverse('plants'))
    else:
        return HttpResponseRedirect(reverse('login'))


def remove_from_garden(request, plant_id):
    CustomerPlant.objects.filter(customer_id=request.user.id, plant_id=plant_id).delete()
    return HttpResponseRedirect(reverse('my_garden'))
