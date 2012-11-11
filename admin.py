from votes.models import Machine, Update
from django.contrib import admin


class MachineAdmin(admin.ModelAdmin):
    fields = ["kind", "number", "state", "last_updated"]
    list_display = ("__unicode__", "state", "last_updated")
    date_hierarchy = "last_updated"

admin.site.register(Machine, MachineAdmin)

admin.site.register(Update)
