from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plants/', views.PlantListView.as_view(), name="plants"),
    path('plant/<int:pk>', views.PlantDetailView.as_view(), name="plant-detail"),
    path('customerplant/<int:pk>', views.CustomerPlantDetailView.as_view(), name="customerplant-detail"),
    path('register/', views.PlantRegisterView.as_view(), name="plant-register"),
]
