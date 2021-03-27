from random import randint
from time import sleep

from django.db.models import Q
from django.http import HttpResponse
import pandas as pd
from app.models import Pharmacist, CustomerVisit, PriceCounter


class CheckPharmacy:

    def enter_pharmacy_counter(self):
        pharm_obj = Pharmacist.objects.all()[0]
        pharm_obj.count_free -= 1
        pharm_obj.save()
        sleep(randint(1, 3))
        pharm_obj.count_free += 1
        pharm_obj.save()

    def enter_cash_counter(self):
        while True:
            cash_obj = PriceCounter.objects.filter(count_free__gte=1)

            if cash_obj[0].count_free >= 1:
                cash_obj[0].count_free -= 1
                cash_obj[0].save()
                sleep(randint(1, 3))
                cash_obj[0].count_free += 1
                cash_obj[0].save()
                break

    def check_pharmacy_free(self):
        pharm_obj = Pharmacist.objects.filter(count_free__gte=1)
        if pharm_obj.exists():
            pharm_obj[0].no_of_waiting += 1
            pharm_obj[0].save()
            return True
        return False


def enter_medical_store(request):
    pharm_obj = Pharmacist.objects.filter(Q(count_free__gte=1) | Q(no_of_waiting__gte=1))
    customer_obj = CustomerVisit.objects.all()[0]
    customer_obj.no_of_customer = customer_obj.no_of_customer + 1
    customer_obj.save()

    if pharm_obj.exists():
        if pharm_obj[0].count_free >= 1:
            obj_ins = CheckPharmacy()
            obj_ins.enter_pharmacy_counter()
            obj_ins.enter_cash_counter()
        else:
            if pharm_obj[0].no_of_waiting >= 1:
                pharm_obj[0].no_of_waiting -= 1
                pharm_obj[0].save()
                while True:
                    obj_ins = CheckPharmacy()
                    call_pharm = obj_ins.check_pharmacy_free()
                    if call_pharm:
                        obj_ins.enter_pharmacy_counter()
                        obj_ins.enter_cash_counter()
                        break

    else:
        customer_obj.customer_denied = customer_obj.customer_denied + 1
        customer_obj.save()
    return HttpResponse("Successfully Process")


def download_report(request):
    response = HttpResponse(content_type="type/csv")
    response["Content-Disposition"] = 'attachment; filename="today_user_report.csv"'
    df = pd.DataFrame(CustomerVisit.objects.all().values('no_of_customer', 'customer_denied'))

    df.to_csv(response, index_label="S.NO")
    return response
