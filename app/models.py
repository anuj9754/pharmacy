from django.db import models

# Create your models here.


class Pharmacist(models.Model):
    waiting_limit = models.IntegerField()
    no_of_waiting = models.IntegerField()
    no_of_counter = models.IntegerField()
    count_free = models.IntegerField()


class PriceCounter(models.Model):
    no_of_counter = models.IntegerField()
    count_free = models.IntegerField()


class CustomerVisit(models.Model):
    no_of_customer = models.IntegerField()
    customer_denied = models.IntegerField()

