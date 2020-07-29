from django.contrib import admin

from raincheck import models


admin.site.register(models.Customer)
admin.site.register(models.Location)
admin.site.register(models.Email)
admin.site.register(models.Plant)
