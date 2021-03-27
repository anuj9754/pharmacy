
import os
import sys

import django


sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pharmacist.settings")
if __name__ == "__main__":
    django.setup()

from app.models import Pharmacist, PriceCounter, CustomerVisit

no_of_counter =3
waiting_limit =3

Pharmacist.objects.create(waiting_limit=waiting_limit*no_of_counter,no_of_waiting=waiting_limit*no_of_counter,no_of_counter=no_of_counter,count_free=no_of_counter)
PriceCounter.objects.create(no_of_counter=no_of_counter,count_free=no_of_counter)
CustomerVisit.objects.create(no_of_customer=0,customer_denied=0)