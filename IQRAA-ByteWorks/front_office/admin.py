from django.contrib import admin
from .models import (Patient_Registration, Address, Doctors_Department, Doctor,Country, State, City, Address)

class AddressInline(admin.StackedInline):
    model = Address
    extra = 0

@admin.register(Patient_Registration)
class PatientAdmin(admin.ModelAdmin):
    inlines = [AddressInline]

@admin.register(Doctors_Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor_count')
    search_fields = ('name',)
    def doctor_count(self, obj):
        return obj.doctors.count()

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department','op_consulting','service_fee')
    list_filter = ('department',)
    search_fields = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name")
    search_fields = ("name", "code")


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")
    search_fields = ("name",)
    list_filter = ("country",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "state")
    search_fields = ("name",)
    list_filter = ("state",)
