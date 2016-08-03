import os
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_standalone.settings")
django.setup()

#from models_standalone.models import SampleModel

from models_standalone.models import Wearable, Wearable_Battery, Wearable_Usage
from models_standalone.models import Sensor, Sensor_Battery, Sensor_Usage

if __name__=="__main__":
        wearable1 = Wearable(name="A1", remarks="Made in Thailand. Please take care of this well.")
        wearable_battery1 = Wearable_Battery(wearable_name=wearable1, battery=60)
        wearable_usage1 = Wearable_Usage(wearable_name=wearable1, used=True)
        wearable1.save()
        wearable_battery1.save()
        wearable_usage1.save()
        pass
        #p = Person(name="Fred Flintstone", shirt_size="L")
