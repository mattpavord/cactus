from django import forms


class CataloguePlantForm(forms.Form):
    plant_name = forms.CharField(max_length=100)
    latin_name = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100)
    country = forms.CharField(max_length=50, required=False)
    image = forms.ImageField()
