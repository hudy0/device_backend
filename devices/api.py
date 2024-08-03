from ninja import NinjaAPI

from devices.models import Device, Location
from devices.schemas import DeviceSchema, LocationSchema

app = NinjaAPI()


@app.get("devices/", response=list[DeviceSchema])
def get_devices(request):
    devices = Device.objects.all()
    return devices


@app.get("locations/", response=list[LocationSchema])
def get_locations(request):
    locations = Location.objects.all()
    return locations
