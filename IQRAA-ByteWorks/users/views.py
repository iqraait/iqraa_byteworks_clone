
# from django.views.generic import TemplateView
# from django.contrib.auth.views import LoginView
# from .forms import EmployeeLoginForm,EmployeeRegistrationForm
# from django.shortcuts import render, redirect
# from django.views import View
# from django.urls import reverse_lazy
# from .models import Employee,Location
# from django.contrib.auth import logout
# from .services import ROLE_REDIRECTS,ROLE_PRIORITY
# from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.conf import settings
# from django.http import JsonResponse
# import logging

# logger = logging.getLogger('registration_logger')





# class EmployeeRegistrationView(View):
#     template_name = 'users/register.html'
#     form_class = EmployeeRegistrationForm
#     success_url = reverse_lazy('users:login')

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
        

#         if form.is_valid():
#             # Print cleaned data (after validation)
#             cleaned_data = form.cleaned_data

#             print("\n=== Cleaned Form Data ===")
#             logger.info(
#                 f"=== Cleaned Form Data ===\n"
#                 f"iqraa_id: {cleaned_data.get('iqraa_id')}\n"
#                 f"username: {cleaned_data.get('username')}\n"
#                 f"department: {cleaned_data.get('department')}\n"
#                 f"location: {cleaned_data.get('location')}\n"
#                 f"password1: {cleaned_data.get('password1')}\n"
#                 f"password2: {cleaned_data.get('password2')}\n"
#             )
#             for key, value in form.cleaned_data.items():
#                 print(f"{key}: {value}")

#             # Save the form and redirect
#             form.save()
#             return redirect(self.success_url)
#         else:
#             # Print form errors if validation fails
#             print("\n=== Form Errors ===")
#             for field, errors in form.errors.items():
#                 print(f"{field}: {errors}")

#         return render(request, self.template_name, {'form': form})






# """Class for the First DashBoard View opening url"""

# class FirstDashBoard(TemplateView):
#     template_name = 'users/main_dashboard.html'





# class EmployeeLoginView(LoginView):
#     template_name = 'users/login.html'
#     form_class = EmployeeLoginForm

#     DEFAULT_REDIRECT = ('users','main_dashboard')

#     def get_redirect_info(self, user):
#         """return redirect based on their role using ROLE_PRIORITY"""

#         print(f"=== DEBUG USER ROLES ===")
#         print(f"User ID: {user.id}")
#         print(f"User iqraa_id: {user.iqraa_id}")
#         print(f"User passsword: {user.password}")
#         print(f"User superuser: {user.is_superuser}")

        
#         for role in ROLE_PRIORITY:  # ["is_incharge","is_superint","is_staff_nurse"]
#             if getattr(user, role, False):  # Checks user.is_incharge, user.is_superint, etc.
#                 print(f"User has role: {role}")
#                 return ROLE_REDIRECTS.get(role, self.DEFAULT_REDIRECT)
        
#         print("No matching role found")
#         return self.DEFAULT_REDIRECT
            

#     def get_success_url(self):
#         user = self.request.user
#         app_name, url_name = self.get_redirect_info(user)
#         return reverse_lazy(f'{app_name}:{url_name}')





# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect(settings.LOGIN_URL)





from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import EmployeeLoginForm,EmployeeRegistrationForm
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Employee,Location
from django.contrib.auth import logout
from .services import ROLE_REDIRECTS,ROLE_PRIORITY
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse






class EmployeeRegistrationView(View):
    template_name = 'users/register.html'
    form_class = EmployeeRegistrationForm
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        

        if form.is_valid():
            # Print cleaned data (after validation)
            print("\n=== Cleaned Form Data ===")
            for key, value in form.cleaned_data.items():
                print(f"{key}: {value}")

            # Save the form and redirect
            form.save()
            return redirect(self.success_url)
        else:
            # Print form errors if validation fails
            print("\n=== Form Errors ===")
            for field, errors in form.errors.items():
                print(f"{field}: {errors}")

        return render(request, self.template_name, {'form': form})






"""Class for the First DashBoard View opening url"""

class FirstDashBoard(TemplateView):
    template_name = 'users/main_dashboard.html'






class EmployeeLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = EmployeeLoginForm

    DEFAULT_REDIRECT = ('users','main_dashboard')

    def get_redirect_info(self, user):
        """return redirect based on their role using ROLE_PRIORITY"""

        print(f"=== DEBUG USER ROLES ===")
        print(f"User ID: {user.id}")
        print(f"User iqraa_id: {user.iqraa_id}")
        print(f"User passsword: {user.password}")
        print(f"User superuser: {user.is_superuser}")

        
        for role in ROLE_PRIORITY:  # ["is_incharge","is_superint","is_staff_nurse"]
            if getattr(user, role, False):  # Checks user.is_incharge, user.is_superint, etc.
                print(f"User has role: {role}")
                return ROLE_REDIRECTS.get(role, self.DEFAULT_REDIRECT)
        
        print("No matching role found")
        return self.DEFAULT_REDIRECT
            

    def get_success_url(self):
        user = self.request.user
        app_name, url_name = self.get_redirect_info(user)
        return reverse_lazy(f'{app_name}:{url_name}')






class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)




















