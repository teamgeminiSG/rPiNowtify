import os
import django
import iotscript



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_standalone.settings")
django.setup()

#from models_standalone.models import SampleModel

from models_standalone.models import Alert

if __name__=="__main__":
	sensorObject = (Sensor.objects.all().filter(name__exact=iotscript.name))[0]
    alert = Alert(sensor=sensorObject)
    with transaction.atomic():
        alert.save()
    	alert.save(using='aws')