from django.shortcuts import render
from django.views import generic

from raincheck.models import Plant, Customer, CustomerPlant


def index(request):
    """View function for home page"""

    num_plants = Plant.objects.all().count()
    num_customers = Customer.objects.all().count()

    context = {
        'num_plants': num_plants,
        'num_customers': num_customers,
    }
    return render(request, 'index.html', context=context)


class PlantListView(generic.ListView):
    model = Plant


class PlantDetailView(generic.DetailView):
    model = Plant


class PlantRegisterView(generic.CreateView):
    model = CustomerPlant
    fields = ['plant']

    def form_valid(self, form):
        print(self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)
