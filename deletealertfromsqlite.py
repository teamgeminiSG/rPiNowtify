import os
import django
from django.db import transaction
#import iotscript

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_standalone.settings")
django.setup()

from models_standalone.models import Alert, Sensor

if __name__=="__main__":
    with transaction.atomic():
        Alert.objects.all().delete()
        #Alert.objects.using('aws').all().delete()