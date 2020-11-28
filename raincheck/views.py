from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic

from raincheck.models import Plant, CustomerPlant, Location
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


@login_required(login_url='/login/')
def catalogue_plant(request):
    if request.method == 'POST':
        form = CataloguePlantForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            plant_name = form.cleaned_data['plant_name']
            location = form.cleaned_data['location']
            location = Location.objects.create(region=location)
            Plant.objects.create(
                location=location,
                name=plant_name,
                image=image,
            )
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = CataloguePlantForm()
    return render(request, 'raincheck/catalogue_plant.html', {'form': form})


@login_required(login_url='/login/')
def my_garden(request):
    user_id = request.user.id
    plant_ids = CustomerPlant.objects.filter(customer_id=user_id).values_list('plant_id', flat=True)
    plants = Plant.objects.filter(id__in=plant_ids)
    if plants.exists():
        return render(request, 'raincheck/plant_list.html', {'plant_list': plants, 'garden': True})
    else:
        message = "Your garden is empty, add plants in the Plants menu"
        return render(request, 'message.html', {"message": message})


def list_plants(request):
    if request.user.is_authenticated:
        garden_plant_ids = CustomerPlant.objects.filter(customer_id=request.user.id)\
            .values_list("plant_id", flat=True)  # to show user what plants they already have
    else:
        garden_plant_ids = []
    context = {
        'plant_list': Plant.objects.all(),
        'garden': False,
        'garden_plant_ids': garden_plant_ids
    }
    return render(request, 'raincheck/plant_list.html', context)


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
