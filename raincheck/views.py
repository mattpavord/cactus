from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from raincheck.models import Plant, CustomerPlant
from raincheck.forms import CataloguePlantForm


def index(request):
    """View function for home page"""

    num_plants = Plant.objects.all().count()
    num_customers = User.objects.all().count()

    context = {
        'num_plants': num_plants,
        'num_customers': num_customers,
    }
    return render(request, 'index.html', context=context)


def catalogue_plant(request):
    if request.method == 'POST':
        form = CataloguePlantForm(request.POST)
        if form.is_valid():
            form.save()
            # do stuff here
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = CataloguePlantForm()
    return render(request, 'signup.html', {'form': form})


class PlantListView(generic.ListView):
    model = Plant


class PlantDetailView(generic.DetailView):
    model = Plant


class CustomerPlantDetailView(generic.DetailView):
    model = CustomerPlant


class PlantRegisterView(generic.CreateView):
    model = CustomerPlant
    fields = ['plant']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)
