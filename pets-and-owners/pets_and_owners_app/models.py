from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=255, blank=False)
    age = models.IntegerField(default=0, validators=[MaxValueValidator(150)], blank=True)
    number_of_pets = models.IntegerField(validators=[MaxValueValidator(50)], blank=True, default = 0)

class Cat(models.Model):
    breed = models.CharField(255, blank=False, default='Unknown')
    age = models.IntegerField(default=0, validators=[MaxValueValidator(50)])
    vaccinated = models.BooleanField(blank=False, default='Unknown')
    description = models.TextField()
    name = models.CharField(max_length=100)

class bird(models.Model):
    name = models.CharField(max_length=255, blank=False, default='No Name')
    age = models.IntegerField(default=0, validators=[MaxValueValidator(200)])
    vaccinated = models.BooleanField()
    description = models.TextField(blank=True, default='No description')
    species = models.CharField()

class Dog(models.Model):
    age = models.IntegerField(default=0, validators=[MaxValueValidator(50)])
    name = models.CharField(max_length=255)
    vaccinated = models.BooleanField(blank=False, default='Unknown')
    description = models.TextField(blank=True, default='No description')
    breed = models.TextField(blank='True', default='Unknown')

class ExoticAnimal(models.Model):
    region_of_origin = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0, validators=[MaxValueValidator(200)])
    type_of_animal = models.CharField(max_length=100)
    vaccinated = models.BooleanField(blank=False, default='Unknown')
