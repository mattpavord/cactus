from django.shortcuts import render
from raincheck.models import Plant, Customer


def index(request):
    """View function for home page"""

    num_plants = Plant.objects.all().count()
    num_customers = Customer.objects.all().count()

    context = {
        'num_plants': num_plants,
        'num_customers': num_customers,
    }
    return render(request, 'index.html', context=context)
