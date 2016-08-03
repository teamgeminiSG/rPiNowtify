import os
import django
from django.db import transaction
#import iotscript



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_standalone.settings")
django.setup()

#from models_standalone.models import SampleModel

from models_standalone.models import Alert, Sensor

if __name__=="__main__":
    sensorObject = Sensor(name="TestSensor", remarks="This is for testing!")
    sensorObject.save(using='aws')
    alert = Alert(sensor=sensorObject)
    with transaction.atomic():
        #alert.save()
    	alert.save(using='aws')



    #wearable1 = Wearable(name="A1", remarks="Made in Thailand. Please take care of this well.")
    #wearable_battery1 = Wearable_Battery(wearable_name=wearable1, battery=60)
   	#wearable_usage1 = Wearable_Usage(wearable_name=wearable1, used=True)
	#wearable1.save()
	#wearable_battery1.save()
	#wearable_usage1.save()
