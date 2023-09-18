from django.db import models
from django.contrib.auth.models import User
from django.forms import TextInput,EmailInput
# Create your models here.
class Feature(models.Model):
    name=models.CharField(max_length=100, default='Names')
    details=models.CharField(max_length=500, default='Details')

class Animal_Shelters(models.Model):
    name=models.CharField(max_length=100, default='Names')
    contact=models.BigIntegerField(default='1111111111')
    address=models.CharField(max_length=500, default='Address' )
    def __str__(self):
        return self.name

class Adoption(models.Model):
    animal_id=models.PositiveIntegerField(default='0',primary_key=True)
    name=models.CharField(max_length=100, default='Names')
    animal_type=models.CharField(max_length=100, default='Animal_Types')
    breed=models.CharField(max_length=500, default='Breeds' )
    age=models.CharField(max_length=200,default='In Months')
    def __str__(self):
        return self.name
        
class AppliedAdoption(models.Model):

    name=models.CharField(max_length=256, default='Your Name')
    email=models.EmailField(max_length=256,unique=True)
    shelter_name=models.CharField(max_length=256,default='Shelter Name')
    animal_id=models.PositiveIntegerField(default='0')
    def __str__(self):
        return self.name

class Volunteering(models.Model):
   animal_shelter_name=models.CharField(max_length=100, default='Names')
   def __str__(self):
        return self.animal_shelter_name
        
class AppliedVolunteering(models.Model):

    name=models.CharField(max_length=256, default='Your Name',)
    email=models.EmailField(max_length=256,unique=True)
    shelter_name=models.CharField(max_length=256,default='Shelter Name')
    def __str__(self):
        return self.name
