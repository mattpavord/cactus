from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from registration import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('raincheck/', include('raincheck.urls')),
    path('signup/', core_views.signup, name='signup'),
    path('', RedirectView.as_view(url='raincheck/', permanent=True)),
    path('login/', core_views.AdminLogin.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
