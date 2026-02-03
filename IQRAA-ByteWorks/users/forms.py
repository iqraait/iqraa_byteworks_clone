# # forms.py
# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
# from .models import Employee,Department,Location
# from django.contrib.auth import get_user_model


# """Employee RegistrationFrom"""

# class EmployeeRegistrationForm(UserCreationForm):
#     department = forms.ModelChoiceField(
#         queryset=Department.objects.all(),
#         required=True,
#         label="Department",
#         widget=forms.Select(
#             attrs={
#                 'class': (
#                     'input-glass w-full bg-white/10 border border-white/15 rounded-xl px-4 py-2 text-white '
#                     'focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400 transition duration-300 ease-in-out'
#                 ),
#                 'id': 'id_department',
#             }
#         )
#     )


#     location = forms.ModelChoiceField(
#         queryset=Location.objects.all(),  # initially empty
#         required=True,
#         label="Location",
#         widget=forms.Select(
#             attrs={
#                 'class': (
#                     'input-glass w-full bg-white/10 border border-white/15 rounded-xl px-4 py-2 text-white '
#                     'focus:outline-none focus:ring-2 focus:ring-green-400 focus:border-green-400 transition duration-300 ease-in-out'
#                 ),
#                 'id': 'id_location',
#             }
#         )
#     )

#     def clean_iqraa_id(self):
#         iqraa_id = self.cleaned_data.get('iqraa_id')
#         if len(iqraa_id) !=6:
#             raise forms.ValidationError("Iqraa ID must be exactly 6 digits.")
#         return iqraa_id
    
    
#     class Meta:
#         model = Employee
#         fields = ('iqraa_id', 'username','department', 'location','password1', 'password2')   # how the form will be set order wise
#         widgets = {
#             'iqraa_id': forms.TextInput(attrs={'placeholder': 'Iqraa ID', 'required': True}),
#             'username': forms.TextInput(attrs={'placeholder': 'Full Name', 'required': True})}
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['iqraa_id'].label = "Iqraa ID"
#         self.fields['iqraa_id'].help_text = "Your unique employee identification number"
#         self.fields['password1'].help_text = None
#         self.fields['username'].label="username"


#     def save(self, commit=True):
#         """Automatically set is_staff_nurse=True if department is nursing."""
#         user = super().save(commit=False)
#         department = self.cleaned_data.get('department')
#         if department and department.department_name.lower() == "nursing_department":
#             user.is_staff_nurse = True
#         if commit:
#             user.save()
#         return user



# from django.contrib.auth import authenticate


# """Employee Login Form"""

# class EmployeeLoginForm(AuthenticationForm):
#     username = forms.IntegerField(
#         label="Iqraa ID",
#         widget=forms.NumberInput(
#             attrs={
#                 'autofocus': True,
#                 'class': 'form-control',
#                 'placeholder': 'Enter Iqraa ID'
#             }
#         )
#     )
#     password = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Password'
#             }
#         )
#     )
    
#     error_messages = {
#         'invalid_login': "Invalid Iqraa ID or password.",
#         'inactive': "This account is inactive. Please contact administrator.",
#         'user_not_found': "Iqraa ID does not exist.",
#         'password_incorrect': "Incorrect password.",
#     }


#     def clean(self):
#         iqraa_id = self.cleaned_data.get('username')
#         print("iqraa id for login",iqraa_id)
#         password =  self.cleaned_data.get('password')
#         print("password of login",password)

#         if iqraa_id and password:
#             print("first checking is correct [if iqraa_id and password]")
#             user =  authenticate(
#                 self.request,username=iqraa_id,
#                 password=password
#             )
#             print("authentication function is works and user is ",user)

#             if user:
#                 print("        user id:",user.id)
#                 print("        iqraa id:",user.iqraa_id)
#                 print("        user password:",user.password)
#             else:
#                 print("authentication failed")
            
#             if user is None:
#                 User = get_user_model()
#                 print(" if user is None  works this line")

#                 if not User.objects.filter(iqraa_id=iqraa_id).exists():
#                     print("user not find")
#                     raise forms.ValidationError(
#                         self.error_messages['user_not_found'],
#                         code = 'user_not_found'
#                     )
#                 print("password_incorrect")
#                 raise forms.ValidationError(
#                     self.error_messages['password_incorrect'],
#                     code='password_incorrect')
        
#             if not user.is_active:
#                 raise forms.ValidationError(
#                     self.error_messages['inactive'],
#                     code='inactive'
#                 )
            
#             self.confirm_login_allowed(user)
#             self.user_cache = user
        
#         print("not iqraa_id and password")
#         return self.cleaned_data



from django.contrib.auth import authenticate
import logging

logger = logging.getLogger("registration_logger")






from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Employee,Department,Location
from django.contrib.auth import get_user_model



"""Employee RegistrationFrom"""

class EmployeeRegistrationForm(UserCreationForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True,
        label="Department",
        widget=forms.Select(
            attrs={
                'class': (
                    'input-glass w-full bg-white/10 border border-white/15 rounded-xl px-4 py-2 text-white '
                    'focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400 transition duration-300 ease-in-out'
                ),
                'id': 'id_department',
            }
        )
    )


    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),  # initially empty
        required=True,
        label="Location",
        widget=forms.Select(
            attrs={
                'class': (
                    'input-glass w-full bg-white/10 border border-white/15 rounded-xl px-4 py-2 text-white '
                    'focus:outline-none focus:ring-2 focus:ring-green-400 focus:border-green-400 transition duration-300 ease-in-out'
                ),
                'id': 'id_location',
            }
        )
    )

    def clean_iqraa_id(self):
        iqraa_id = self.cleaned_data.get('iqraa_id')
        if len(iqraa_id) !=6:
            raise forms.ValidationError("Iqraa ID must be exactly 6 digits.")
        return iqraa_id
    

    def clean(self):
        cleaned_data = super().clean()

        # Log only if form is valid (no errors)
        if not self.errors:
            logger.info("=== Cleaned Form Data ===")
            for key, value in cleaned_data.items():
                if key in ["password1", "password2"]:
                    logger.info(f"{key}: {value}")
                else:
                    logger.info(f"{key}: {value}")

        return cleaned_data
    
    class Meta:
        model = Employee
        fields = ('iqraa_id', 'username','department', 'location','password1', 'password2')   # how the form will be set order wise
        widgets = {
            'iqraa_id': forms.TextInput(attrs={'placeholder': 'Iqraa ID', 'required': True}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'required': True})}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['iqraa_id'].label = "Iqraa ID"
        self.fields['iqraa_id'].help_text = "Your unique employee identification number"
        self.fields['password1'].help_text = None
        self.fields['username'].label="username"


    def save(self, commit=True):
        """Automatically set is_staff_nurse=True if department is nursing."""
        user = super().save(commit=False)
        department = self.cleaned_data.get('department')
        if department and department.department_name.lower() == "nursing department":
            user.is_staff_nurse = True
        if commit:
            user.save()
        return user






"""Employee Login Form"""

class EmployeeLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Iqraa ID",
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'Enter Iqraa ID',
                'inputmode': 'numeric',
                'pattern': '[0-9]*'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }
        )
    )

    error_messages = {
        'invalid_login': "Invalid Iqraa ID or password.",
        'inactive': "This account is inactive. Please contact administrator.",
        'user_not_found': "Iqraa ID does not exist.",
        'password_incorrect': "Incorrect password.",
    }


    def clean(self):
        iqraa_id = self.cleaned_data.get('username')
        print('iqraa_id inside clean function',iqraa_id)
        password = self.cleaned_data.get('password')
        print('password inside clean function',password)

        if iqraa_id and password:
            print("enter inside the if function of authenticate method")
            user = authenticate(
                self.request,
                username=iqraa_id,
                password=password
            )
            print(f"\nStep 3: authenticate() returned: {user}")
            if user:
                print(f"       User ID: {user.id}")
                print(f"       User iqraa_id: {user.iqraa_id}")
                print(f"       User type: {type(user).__name__}")
            else:
                print(f"       Authentication FAILED - returned None")

            if user is None:
                User = get_user_model()
                print("if user is None: works this line")


                if not User.objects.filter(iqraa_id=iqraa_id).exists():
                    logger.warning(f"Login failed: User not found (Iqraa ID={iqraa_id})")
                    raise forms.ValidationError(
                        self.error_messages['user_not_found'],
                        code='user_not_found'
                    )

                # User exists but password wrong

                logger.warning(f"Login failed: Wrong password (Iqraa ID={iqraa_id})")
                raise forms.ValidationError(
                    self.error_messages['password_incorrect'],
                    code='password_incorrect'
                )
            print("if user is not None")
            # User exists but inactive
            if not user.is_active:
                logger.warning(f"Login failed: Inactive user (Iqraa ID={iqraa_id})")
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive'
                )

            self.confirm_login_allowed(user)
            self.user_cache = user  # Store user for get_user() method


        return self.cleaned_data