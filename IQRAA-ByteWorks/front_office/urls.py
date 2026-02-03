from django.urls import path
from .views import (PatientRegisterView,PatientsListView,PatientBillPDFView)



app_name = 'front_office'  # Must have this namespace



urlpatterns = [
        path('', PatientRegisterView.as_view(), name="patient_register"),
        path("patients", PatientsListView.as_view(), name="patients_list"),
        path("patient/<int:pk>/bill/pdf/", PatientBillPDFView.as_view(), name="patient_bill_pdf"),


]

















