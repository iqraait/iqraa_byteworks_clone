from django import forms
from django.urls import reverse_lazy
from .models import Patient_Registration, Address

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient_Registration
        fields = [
            "mobile_number",
            "first_name",
            "middle_name",
            "whatapp_number",
            "date_of_birth",
            "gender",
            "patient_type",
            "title",
            "appoinment_date",
            "department",
            "doctor_vist",
            "registration_type",
            "doctor_name",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control","required": "required"}),
            "appoinment_date": forms.DateInput(attrs={"type": "date", "class": "form-control","required": "required"}),
            "mobile_number": forms.TextInput(attrs={"type": "tel", "class": "form-control", "placeholder": "+91 ","required": "required"}),
            "whatsapp_number": forms.TextInput(attrs={"type": "tel", "class": "form-control", "placeholder": "+91 ",}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter first name","required": "required"}),
            "middle_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "optional)"
            }),
            "date_of_birth": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
                "required": "required"
            }),

            "appoinment_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
                "required": "required"
            }),


        }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        select_fields = [
            "title", "gender", "patient_type", "department",
            "doctor_vist", "doctor_name", "registration_type"
        ]

        for field in select_fields:
            if field in self.fields:
                self.fields[field].widget.attrs.update({
                    "class": "form-control",
                    "required": "required"
                })

                current_choices = list(self.fields[field].choices)
                if current_choices and current_choices[0][0] == '':
                    current_choices.pop(0)
                self.fields[field].choices = [("", "--Select--")] + current_choices
        
class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ["address_line_1", "address_line_2", "city", "state", "country", "pincode"]


        widgets = {
            "address_line_1": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter address line 1",
                "required": "required"
            }),
            "address_line_2": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter address line 2 (optional)"
            }),
            "city": forms.Select(attrs={
                "class": "form-control",
                "required": "required"
            }),
            "state": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter state",
                "required": "required"
            }),
            "country": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter country",
                "required": "required"
            }),
            "pincode": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter pincode",
                "required": "required"
            }),
        }

