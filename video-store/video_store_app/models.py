from django.db import models

# Create your models here.
class Client(models.Model):
    account_type = models.CharField(max_length=20)
    email = models.EmailField()
    active = models.BooleanField()

class Video(models.Model):
    title = models.CharField(max_length=100)
    in_stock = models.BigIntegerField(default=1)
    rating = models.CharField(max_length=1)

class Person(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    middle_init = models.CharField(max_length=1, blank=True)
    age = models.IntegerField(blank=False, default=18)

class Address(models.Model):
    street = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=2)
    appt_num = models.IntegerField()

class store(models.Model):
    name = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    rating = models.FloatField()
    owner = models.IntegerField()