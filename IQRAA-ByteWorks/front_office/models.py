from django.db import models
from users.models import BaseModel
from .choices import (Gender,Patient_type,Title,Visit,Registration_type,City,State)
import datetime



class Doctors_Department(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name



class Doctor(BaseModel):  # Changed from Doctors to Doctor (singular)
    name = models.CharField(max_length=120,unique=True)
    department = models.ForeignKey(
        Doctors_Department,
        on_delete=models.SET_NULL,  # Doctor remains if department is deleted
        null=True,
        blank=True,
        related_name='doctors'  # Access via department.doctors.all()
    )
    op_consulting = models.IntegerField(blank=True,null=True)
    service_fee = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.name} ({self.department.name if self.department else 'No Department'})"







class Patient_Registration(BaseModel):
    mobile_number = models.CharField(max_length=12,blank=False,null=False)
    first_name = models.CharField(max_length=100,blank=False,null=False)
    middle_name = models.CharField(max_length=100,blank=True,null=True)
    whatapp_number = models.CharField(max_length=12,blank=True,null=True)
    date_of_birth = models.DateField(blank=False,null=False)
    gender = models.CharField(choices=Gender.choices,blank=False,null=False,max_length=1)
    patient_type = models.CharField(choices=Patient_type.choices,blank=False,null=False,max_length=2)
    title = models.CharField(choices=Title.choices,blank=False,null=False,max_length=4)
    appoinment_date = models.DateField(default=datetime.date.today)
    department = models.ForeignKey(Doctors_Department,on_delete=models.SET_NULL,blank=True,null=True)
    doctor_vist = models.CharField(choices=Visit.choices,max_length=4,blank=True,null=True)
    registration_type = models.CharField(choices=Registration_type.choices,max_length=2,blank=True,null=True)
    doctor_name = models.ForeignKey(Doctor,on_delete=models.SET_NULL,blank=True,null=True)



    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f"{self.first_name} ({self.mobile_number})"



class Country(models.Model):
    code = models.CharField(max_length=5, unique=True)  # e.g., "IN"
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("country", "name")

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("state", "name")

    def __str__(self):
        return f"{self.name}, {self.state.name}"





class Address(BaseModel):
    patient = models.OneToOneField(
        Patient_Registration,
        on_delete=models.CASCADE,
        related_name='address'
    )
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True,default=12)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    pincode = models.CharField(max_length=8)






























