# from django import forms
# from .models import Form1_assement,StaffProfile
# from .constants_data import WARD_FORM,DEFAULT_FORM_HEADING
# from .models import Employee
# import re




# class StaffInformation(forms.ModelForm):
#     class  Meta:
#         model = StaffProfile
#         fields = ['employee','designation','date_of_join']
#         widgets = {
#             'date_of_join': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
#         }


#     def __init__(self,*args,**kwargs):
#         user = kwargs.pop('user', None)  # grab the logged-in user
#         super().__init__(*args,**kwargs)
#         self.fields['date_of_join'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']

#         if user:
#             self.fields['employee'].queryset = Employee.objects.filter(location=user.location)







# class BaseAssessmentForm(forms.ModelForm):
#     """Common save logic for both forms"""
#     def save(self, commit=True, staff=None, evaluator=None, instance=None, evaluation_period=None):
#         # Use provided instance or create a new one
#         if instance is None:
#             instance = super().save(commit=False)

#         # Merge existing data with cleaned_data
#         data_dict = instance.data.copy() if instance.data else {}
#         for field_name, field in self.fields.items():
#             if field_name == 'evaluation_period':
#                 continue
#             val = self.cleaned_data.get(field_name)
#             data_dict[field_name] = val

#         # Recalculate total_score and total_items based on full data_dict
#         total_score = 0
#         total_items = 0
#         for value in data_dict.values():
#             try:
#                 score = int(value)
#             except (ValueError, TypeError):
#                 score = 0
#             total_score += score
#             total_items += 1

#         instance.data = data_dict
#         instance.total_score = total_score
#         instance.percentage = round((total_score / (total_items * 4)) * 100, 2) if total_items else 0

#         # Only set these if provided

#         if staff:
#             instance.staff_profile = staff
#         if evaluator:
#             instance.evaluator_name = evaluator
#         if evaluation_period:
#             instance.evaluation_period = evaluation_period

#         if commit:
#             instance.save()
#         return instance

        
        

# class AssementFormDefault(BaseAssessmentForm):
#     RATING_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]

#     class Meta:
#         model = Form1_assement
#         fields = ['evaluation_period']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for section, items in DEFAULT_FORM_HEADING.items():
#             for i in items:
#                 field_name = f"{section}_{re.sub(r'[^a-zA-Z0-9_]+', '_', i)[:50]}"
#                 self.fields[field_name] = forms.ChoiceField(
#                     label=i,
#                     choices=self.RATING_CHOICES,
#                     widget=forms.RadioSelect(attrs={'class': 'rating-radio'}),
#                     required=True,
#                 )

#         self.sections = DEFAULT_FORM_HEADING




# # ----------------- 2️⃣ Ward Assessment Form -----------------
# class WardAssessmentForm(BaseAssessmentForm):
#     class Meta:
#         model = Form1_assement
#         fields = []

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for section, descriptions in WARD_FORM.items():
#             field_name = section.replace(" ", "_").replace(":", "").replace("’", "")
#             self.fields[field_name] = forms.CharField(
#                 label=section,
#                 widget=forms.TextInput(attrs={
#                     'class': 'border border-gray-300 rounded p-2 w-full',
#                     'placeholder': 'Enter mark '
#                 }),
#                 required=False,
#             )

#         self.section_descriptions = WARD_FORM













from django import forms
from .models import Form1_assement,StaffProfile
from .constants_data import WARD_FORM,DEFAULT_FORM_HEADING
from .models import Employee
import re




class StaffInformation(forms.ModelForm):
    class  Meta:
        model = StaffProfile
        fields = ['employee','designation','date_of_join']
        widgets = {
            'date_of_join': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
        }


    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user', None)  # grab the logged-in user
        super().__init__(*args,**kwargs)
        self.fields['date_of_join'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']

        if user:
            self.fields['employee'].queryset = Employee.objects.filter(location=user.location)







class BaseAssessmentForm(forms.ModelForm):
    """Common save logic for both forms"""
    def save(self, commit=True, staff=None, evaluator=None, instance=None, evaluation_period=None):
        # Use provided instance or create a new one
        if instance is None:
            instance = super().save(commit=False)

        # Merge existing data with cleaned_data
        data_dict = {} 
        for field_name, field in self.fields.items():
            if field_name == 'evaluation_period':
                continue 
            val = self.cleaned_data.get(field_name)
            data_dict[field_name] = val



        existing_data = instance.data or {}
        existing_data.update(data_dict)
        instance.data = existing_data

        # 🔍 DEBUG
        print("\n📦 FINAL instance.data KEYS:")
        for k in instance.data:
            print("   ✔", k)

        print("📊 TOTAL QUESTIONS:", len(instance.data))

        total_score = 0
        total_items = 0



        for key, value in instance.data.items():
            try:
                total_score += int(value)
                total_items += 1
            except (ValueError, TypeError):
                print("⚠️ Skipped non-numeric:", key, value)

        print("🧮 TOTAL ITEMS COUNTED:", total_items)
        print("🧮 TOTAL SCORE:", total_score)

        instance.total_score = total_score
        instance.percentage = round(
            (total_score / (total_items * 4)) * 100, 2
        ) if total_items else 0


        if staff:
            instance.staff_profile = staff
        if evaluator:
            instance.evaluator_name = evaluator
        if evaluation_period:
            instance.evaluation_period = evaluation_period

        if commit:
            instance.save()
        return instance

        
        

class AssementFormDefault(BaseAssessmentForm):
    RATING_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]

    class Meta:
        model = Form1_assement
        fields = ['evaluation_period']

    def __init__(self, *args, **kwargs):
        print("\n🔹 AssementFormDefault __init__ started")

        super().__init__(*args, **kwargs)

        for section, items in DEFAULT_FORM_HEADING.items():
            print(f"\n➡️ Processing SECTION: {section}")
            print("Items:", items)

            for i in items:
                print(f"   🔸 Raw item:", i)
                cleaned_item = re.sub(r'[^a-zA-Z0-9_]+', '_', i)
                print(f"   🧼 Cleaned item:", cleaned_item)


                field_name = f"{section}_{re.sub(r'[^a-zA-Z0-9_]+', '_', i)[:50]}"
                print(f"   🏷️ Final field_name:", field_name)

                self.fields[field_name] = forms.ChoiceField(
                    label=i,
                    choices=self.RATING_CHOICES,
                    widget=forms.RadioSelect(attrs={'class': 'rating-radio'}),
                    required=True,
                )
                
                print("===========================================================")

                print(f"   ✅ Field ADDED:", field_name)

                print("===========================================================")



        self.sections = DEFAULT_FORM_HEADING
        print("\n🧾 section_descriptions SET")

        print("\n🎯 FINAL FIELD LIST IN FORM:")
        for name in self.fields:
            print("   ✔", name)

        print("#################### class AssementFormDefault(BaseAssessmentForm): INIT END ##############\n")






# ----------------- 2️⃣ Ward Assessment Form -----------------
class WardAssessmentForm(BaseAssessmentForm):
    class Meta:
        model = Form1_assement
        fields = []

    def __init__(self, *args, **kwargs):
        print("\n================ WardAssessmentForm INIT START ================")

        print("📥 Raw args:", args)
        print("📦 Raw kwargs:", kwargs)
        super().__init__(*args, **kwargs)
        print("\n✅ After super().__init__()")
        print("Initial self.fields:", list(self.fields.keys()))

        print("\n📊 WARD_FORM content:")

        for section, descriptions in WARD_FORM.items():
            print("\n------------------------------------------------")
            print("➡️ ORIGINAL SECTION TEXT:", section)
            print("➡️ DESCRIPTION VALUE:", descriptions)


            field_name = section
            print("   1️⃣ Starting field_name:", field_name)

            field_name = field_name.replace(" ", "_")
            print("   2️⃣ After space replace:", field_name)

            field_name = field_name.replace(":", "")
            print("   3️⃣ After colon remove:", field_name)

            field_name = field_name.replace("’", "")
            print("   4️⃣ After special quote remove:", field_name)

            print("🏷️ FINAL FIELD NAME:", field_name)



            self.fields[field_name] = forms.CharField(
                label=section,
                widget=forms.TextInput(attrs={
                    'class': 'border border-gray-300 rounded p-2 w-full',
                    'placeholder': 'Enter mark '
                }),
                required=False,
            )

            print("✅ FIELD ADDED TO FORM:", field_name)


        self.section_descriptions = WARD_FORM
        print("\n🧾 section_descriptions SET")

        print("\n🎯 FINAL FIELD LIST IN FORM:")
        for name in self.fields:
            print("   ✔", name)

        print("================ WardAssessmentForm INIT END =================\n")




