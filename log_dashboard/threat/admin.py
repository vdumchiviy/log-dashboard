from django.contrib import admin
from .models import ThreatCategory, Threat
from log.models import Log
from random import choice, randint
# Register your models here.


class ThreatAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        server_name = (''.join(choice("abc") for i in range(3)))
        max_rows = randint(1, 5)
        for x in range(max_rows):
            log = Log(server_name=server_name,
                      threat=obj, comment=f"comment {x}")
            log.save()


admin.site.register(ThreatCategory)
admin.site.register(Threat, ThreatAdmin)
