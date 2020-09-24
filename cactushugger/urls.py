from django.contrib import admin
from django.urls import path, include
from registration import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('raincheck/', include('raincheck.urls')),
    path('signup/', core_views.signup, name='signup'),
    path('login/', core_views.AdminLogin.as_view(), name='login'),
]
