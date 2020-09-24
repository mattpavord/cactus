from django import forms

from raincheck.models import CustomerPlant, Plant


class PlantRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerPlant

    plant = forms.ModelChoiceField(queryset=Plant.objects.all())
