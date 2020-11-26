from django import forms


class CataloguePlantForm(forms.Form):
    plant_name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    image = forms.ImageField()
