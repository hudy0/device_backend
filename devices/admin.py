from django.contrib import admin

from devices.models import Location, Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )


admin.site.register(Device, DeviceAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Location, LocationAdmin)
