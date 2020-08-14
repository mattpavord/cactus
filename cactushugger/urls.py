from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from registration import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('raincheck/', include('raincheck.urls')),
    path('', RedirectView.as_view(url='raincheck/', permanent=True)),
    path('registration/', core_views.signup),
]
