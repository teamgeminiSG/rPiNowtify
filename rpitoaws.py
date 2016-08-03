import os
import django
from django.db import transaction



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_standalone.settings")
django.setup()

#from models_standalone.models import SampleModel

from models_standalone.models import Wearable, Wearable_Battery, Wearable_Usage
from models_standalone.models import Sensor, Sensor_Battery, Sensor_Usage
from models_standalone.models import Alert

if __name__=="__main__":


    wearableUnique = []
    wearableUsage = []
    wearableBattery = []
    wearableLocation = []

	for instance in Wearable.objects.all():
        wearableUnique.append(instance)

    for wearableObject in wearableUnique:
        wearableUsage.append(WearableUsage.objects.all().filter(wearable_name__exact=wearableObject).order_by('updated').first())
        wearableBattery.append(WearableBattery.objects.all().filter(wearable_name__exact=wearableObject).order_by('updated').first())


    sensorUnique = []
    sensorUsage = []
    sensorBattery = []
    sensorLocation = []

    for instance in Sensor.objects.all():
        sensorUnique.append(instance)

    for sensorObject in sensorUnique:
        sensorUsage.append(SensorUsage.objects.all().filter(sensor_name__exact=sensorObject).order_by('updated').first())
        sensorBattery.append(SensorBattery.objects.all().filter(sensor_name__exact=sensorObject).order_by('updated').first())



    with transaction.atomic():

		for instance in wearableUnique:
    		instance.save(using='aws')

    	for instance in wearableUsage:
    		instance.save(using='aws')

    	for instance in wearableBattery:
    		instance.save(using='aws')

		for instance in sensorUnique:
    		instance.save(using='aws')

    	for instance in sensorUsage:
    		instance.save(using='aws')

    	for instance in sensorBattery:
    		instance.save(using='aws')

    	queryTime = datetime.datetime.now() - datetime.timedelta(minutes=1)

    	WearableUsage.objects.all().exclude(updated__gt=queryTime).delete()
    	WearableBattery.objects.all().exclude(updated__gt=queryTime).delete()
    	SensorUsage.objects.all().exclude(updated__gt=queryTime).delete()
    	SensorBattery.objects.all().exclude(updated__gt=queryTime).delete()