from django.contrib import admin
from .models import ThreatCategory, Threat
# Register your models here.


class ThreatAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


admin.site.register(ThreatCategory)
admin.site.register(Threat, ThreatAdmin)
