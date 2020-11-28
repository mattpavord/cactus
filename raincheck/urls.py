from django.urls import path
from . import views, actions

urlpatterns = [
    path('', views.index, name='index'),
    path('plants/', views.list_plants, name="plants"),
    path('my_garden/', views.my_garden, name="my_garden"),
    path('plant/<int:pk>', views.PlantDetailView.as_view(), name="plant-detail"),
    path('customerplant/<int:pk>', views.CustomerPlantDetailView.as_view(), name="customerplant-detail"),
    path('register/', views.PlantRegisterView.as_view(), name="plant-register"),
    path('catalogue_plant/', views.catalogue_plant, name='catalogue-plant'),
    path('add_to_garden/<int:plant_id>', actions.add_to_garden, name="add_to_garden"),
    path('remove_from_garden/<int:plant_id>', actions.remove_from_garden, name="remove_from_garden"),
]
