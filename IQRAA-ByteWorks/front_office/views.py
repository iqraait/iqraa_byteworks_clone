from django.views import View
from django.shortcuts import render, redirect
from .forms import PatientRegistrationForm, AddressForm
from .models import Patient_Registration,City
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .service import generate_patient_bill_pdf
from django.http import JsonResponse
from . models import Doctor


class PatientRegisterView(View):
    template_name = "front_office/patientregister.html"

    def get(self, request, *args, **kwargs):
        patient_form = PatientRegistrationForm()
        address_form = AddressForm()
        cities = City.objects.select_related("state__country").all()

        return render(request, self.template_name, {
            "patient_form": patient_form,
            "address_form": address_form,
            "cities":cities
        })

    def post(self, request, *args, **kwargs):
        patient_form = PatientRegistrationForm(request.POST)
        address_form = AddressForm(request.POST)

        if patient_form.is_valid() and address_form.is_valid():
            patient = patient_form.save()
            address = address_form.save(commit=False)
            address.patient = patient
            address.save()
            return redirect("front_office:patients_list")

        return render(request, self.template_name, {
            "patient_form": patient_form,
            "address_form": address_form,
        })



class PatientsListView(ListView):
    model = Patient_Registration
    template_name = "front_office/patients_list.html"
    context_object_name = "patients"
    ordering = ["-created"]  # latest first



class PatientBillPDFView(View):
    def get(self, request, pk, *args, **kwargs):
        patient = get_object_or_404(Patient_Registration, pk=pk)
        return generate_patient_bill_pdf(patient)
