# from django.views.generic import TemplateView,DetailView
# from django.contrib import messages
# from django.shortcuts import redirect, render
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Form1_assement,StaffProfile,Employee
# from django.views.generic import ListView,View
# from django.shortcuts import get_object_or_404, redirect
# from django.urls import reverse_lazy
# from django.utils.timezone import now, timedelta
# from django.db import transaction
# from .dashboard import get_incharge_dashboard_data
# from .forms import StaffInformation,AssementFormDefault,WardAssessmentForm
# from django.views.generic.edit import FormView  # <-- make sure this is imported
# from .constants_data import WARD_FORM




# today = now().date()
# start_of_week = today - timedelta(days=today.weekday())





# class InchargeDashboard(LoginRequiredMixin,TemplateView):  # incharge dashboard Tempalte
#     template_name = 'nursing_admin/inchargeTemplate.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         employee = self.request.user
#         dashboard_data = get_incharge_dashboard_data(employee)  #import from and save the function from the dashboard.py
#         context.update(dashboard_data)     #update into context
#         return context
    





# class PreviewForm(LoginRequiredMixin,TemplateView):
#     template_name = "nursing_admin/from2.html"
#     success_url = "nursing_department:InchargeDashboard"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form1'] = StaffInformation(prefix='form1',user=self.request.user)  # Note: Don't instantiate with () in class attribute
#         context['form2'] = AssementFormDefault(prefix='form2')
#         context['form3'] = WardAssessmentForm(prefix='form3')
#         context['section_descriptions'] = context['form3'].section_descriptions

        
#         return context
    
#     def post(self, request, *args, **kwargs):
#         form1 = StaffInformation(request.POST, prefix="form1",user=self.request.user)  # Staff form
#         form2 = AssementFormDefault(request.POST, prefix="form2")  # Assessment form
#         form3 = WardAssessmentForm(request.POST, prefix="form3")





#         if form1.is_valid() and form2.is_valid() and form3.is_valid():

#             staff_instance = form1.save() 
#             print("\n=== Cleaned Form Data Form1 ===")
#             for key, value in form1.cleaned_data.items():
#                 print(f"{key}: {value}")


#             print("\n=== Cleaned Form Data ===")
#             for key, value in form2.cleaned_data.items():
#                 print(f"{key}: {value}")

#             for key,value in form3.cleaned_data.items():
#                 print(f"{key}: {value}")



                
#             # Get evaluator from logged-in user
#             evaluator_instance = request.user

#             from django.db import transaction

#             with transaction.atomic():
#                 assessment_instance = form2.save(staff=staff_instance,evaluator=evaluator_instance)
#                 form3.save(instance=assessment_instance)
#             messages.success(request, "Form submitted successfully!")
#             return redirect(self.success_url)


#         return render(request, self.template_name, {
#             'form1': form1,
#             'form2':form2,
#             'form3':form3,
#             'section_descriptions': form3.section_descriptions,  # ✅ Add here too

#         })












# class AdminDashboardView(TemplateView):   # admin dashboard
#     model = Form1_assement
#     template_name = 'nursing_admin/DashBoardForAdminAccess.html'

#     def get_context_data(self, **kwargs): # pass the values
#         print("DEBUG user:", self.request.user)
#         print("DEBUG is_authenticated:", self.request.user.is_authenticated)
#         context = super().get_context_data(**kwargs)
#         context['assessment_count']=Form1_assement.objects.count()
#         context['pending_assessments'] = Form1_assement.objects.filter(is_approved=False).count()
#         context['completed_assessments'] = Form1_assement.objects.filter(is_approved=True).count()
#         context['new_in_this_week'] = Form1_assement.objects.filter(
#             evaluation_date__gte=start_of_week
#         ).count()        

#         if context['assessment_count']>0:
#             context['completion_rate'] = round(
#                 context['completed_assessments']*100/context['assessment_count'],2
#             )
#         else:
#             context['completion_rate']=0
    
#         context['assessments'] = (
#             Form1_assement.objects
#             .select_related("evaluator_name", "staff_profile")
#             .filter(staff_acknowdged=True)
#             .order_by('-evaluation_date')
#         )

#         if self.request.user.is_authenticated and hasattr(self.request.user, "iqraa_id"):
#             context["iqraa_id"] = self.request.user.iqraa_id

        
#         return context



# class StaffApproveAssementView(View):
#     def post(self,request,pk):
#         assessment = get_object_or_404(Form1_assement,pk=pk)
#         assessment.staff_acknowdged = True
#         assessment.save()
#         messages.success(request, "Form acknowledged successfully!")
#         return redirect("nursing_department:staff_approve_assessment",pk=pk)        




# class ApproveAssementView(View):
#     def post(self,request,pk):
#         assessment = get_object_or_404(Form1_assement,pk=pk)
#         assessment.is_approved = True
#         assessment.save()
#         messages.success(request, "Form Approved successfully!")
#         return redirect("nursing_department:nursing_admin_dashboard")        




# class AssmentDetailedView(DetailView):
#     model=Form1_assement
#     template_name = "nursing_admin/detailviewed.html"
#     context_object_name = "assessment"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form_data'] = self.object.data
#         return context
    




# class StaffFormsView(LoginRequiredMixin, ListView):
#     model = Form1_assement
#     template_name = 'nursing_admin/my_forms.html'
#     context_object_name = 'staff_forms'


#     def get_queryset(self):
#         user = self.request.user  # logged-in Employee

#         # Only for staff nurse
#         if user.is_staff_nurse:
#             # Get all StaffProfiles linked to this employee
#             staff_profiles = StaffProfile.objects.filter(employee=user)
#             return Form1_assement.objects.filter(staff_profile__in=staff_profiles)

#         # Optional: incharge or superusers see all
#         return Form1_assement.objects.all()



# class Form1AssessmentDetailView(DetailView):
#     model = Form1_assement
#     template_name = "nursing_admin/forms_detail.html"
#     context_object_name = "assessment"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["staff"] = self.object.staff_profile
#         context["evaluator"] = self.object.evaluator_name
#         return context


# class InchargeStaffViewPanel(LoginRequiredMixin,ListView):
#     model = Employee
#     template_name = "nursing_admin/stafflistInsideInchargePage.html"
#     context_object_name = "staff_list"

#     def get_queryset(self):
#         user=self.request.user
#         staff_list_orm = Employee.objects.filter(location=user.location)
#         return staff_list_orm





# class InchargeFormsListView(View):
#     template_name = "nursing_admin/form_listing.html"

#     def get(self, request):
#         # ✅ Filter only forms submitted by the logged-in incharge
#         if request.user.is_authenticated and request.user.is_incharge:
#             forms = Form1_assement.objects.filter(evaluator_name=request.user).order_by('-evaluation_date')
#         else:
#             forms = []

#         return render(request, self.template_name, {'forms': forms})
    


from django.views.generic import TemplateView,DetailView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Form1_assement,StaffProfile,Employee
from django.views.generic import ListView,View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.timezone import now, timedelta
from django.db import transaction
from .dashboard import get_incharge_dashboard_data
from .forms import StaffInformation,AssementFormDefault,WardAssessmentForm
from django.views.generic.edit import FormView  # <-- make sure this is imported
from .constants_data import WARD_FORM




today = now().date()
start_of_week = today - timedelta(days=today.weekday())





class InchargeDashboard(LoginRequiredMixin,TemplateView):  # incharge dashboard Tempalte
    template_name = 'nursing_admin/inchargeTemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.request.user
        dashboard_data = get_incharge_dashboard_data(employee)  #import from and save the function from the dashboard.py
        context.update(dashboard_data)     #update into context
        return context
    





class WardAssementForm(LoginRequiredMixin,TemplateView):
    template_name = "nursing_admin/from2.html"
    success_url = "nursing_department:InchargeDashboard"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form1'] = StaffInformation(prefix='form1',user=self.request.user)  # Note: Don't instantiate with () in class attribute
        context['form2'] = AssementFormDefault(prefix='form2')
        context['form3'] = WardAssessmentForm(prefix='form3')
        context['section_descriptions'] = context['form3'].section_descriptions

        
        return context
    
    def post(self, request, *args, **kwargs):
        form1 = StaffInformation(request.POST, prefix="form1",user=self.request.user)  # Staff form
        form2 = AssementFormDefault(request.POST, prefix="form2")  # Assessment form
        form3 = WardAssessmentForm(request.POST, prefix="form3")





        if form1.is_valid() and form2.is_valid() and form3.is_valid():

            staff_instance = form1.save() 
            print("\n=== Cleaned Form Data Form1 ===")
            for key, value in form1.cleaned_data.items():
                print(f"{key}: {value}")


            print("\n=== Cleaned Form Data ===")
            for key, value in form2.cleaned_data.items():
                print(f"{key}: {value}")
            
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            for key,value in form3.cleaned_data.items():
                print(f"{key}: {value}")



                
            # Get evaluator from logged-in user
            evaluator_instance = request.user

            from django.db import transaction

            with transaction.atomic():
                assessment_instance = form2.save(staff=staff_instance,evaluator=evaluator_instance)
                form3.save(instance=assessment_instance)
            messages.success(request, "Form submitted successfully!")
            return redirect(self.success_url)


        return render(request, self.template_name, {
            'form1': form1,
            'form2':form2,
            'form3':form3,
            'section_descriptions': form3.section_descriptions,  # ✅ Add here too

        })












class AdminDashboardView(TemplateView):   # admin dashboard
    model = Form1_assement
    template_name = 'nursing_admin/DashBoardForAdminAccess.html'

    def get_context_data(self, **kwargs): # pass the values
        print("DEBUG user:", self.request.user)
        print("DEBUG is_authenticated:", self.request.user.is_authenticated)
        context = super().get_context_data(**kwargs)
        context['assessment_count']=Form1_assement.objects.count()
        context['pending_assessments'] = Form1_assement.objects.filter(is_approved=False).count()
        context['completed_assessments'] = Form1_assement.objects.filter(is_approved=True).count()
        context['new_in_this_week'] = Form1_assement.objects.filter(
            evaluation_date__gte=start_of_week
        ).count()        

        if context['assessment_count']>0:
            context['completion_rate'] = round(
                context['completed_assessments']*100/context['assessment_count'],2
            )
        else:
            context['completion_rate']=0
    
        context['assessments'] = (
            Form1_assement.objects
            .select_related("evaluator_name", "staff_profile")
            .filter(staff_acknowdged=True)
            .order_by('-evaluation_date')
        )

        if self.request.user.is_authenticated and hasattr(self.request.user, "iqraa_id"):
            context["iqraa_id"] = self.request.user.iqraa_id

        
        return context



class StaffApproveAssementView(View):
    def post(self,request,pk):
        assessment = get_object_or_404(Form1_assement,pk=pk)
        assessment.staff_acknowdged = True
        assessment.save()
        messages.success(request, "Form acknowledged successfully!")
        return redirect("nursing_department:staff_approve_assessment",pk=pk)        




class ApproveAssementView(View):
    def post(self,request,pk):
        assessment = get_object_or_404(Form1_assement,pk=pk)
        assessment.is_approved = True
        assessment.save()
        messages.success(request, "Form Approved successfully!")
        return redirect("nursing_department:nursing_admin_dashboard")        




class AssmentDetailedView(DetailView):
    model=Form1_assement
    template_name = "nursing_admin/detailviewed.html"
    context_object_name = "assessment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_data'] = self.object.data
        return context
    




class StaffFormsView(LoginRequiredMixin, ListView):
    model = Form1_assement
    template_name = 'nursing_admin/my_forms.html'
    context_object_name = 'staff_forms'


    def get_queryset(self):
        user = self.request.user  # logged-in Employee

        # Only for staff nurse
        if user.is_staff_nurse:
            # Get all StaffProfiles linked to this employee
            staff_profiles = StaffProfile.objects.filter(employee=user)
            return Form1_assement.objects.filter(staff_profile__in=staff_profiles)

        # Optional: incharge or superusers see all
        return Form1_assement.objects.all()



class Form1AssessmentDetailView(DetailView):
    model = Form1_assement
    template_name = "nursing_admin/forms_detail.html"
    context_object_name = "assessment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["staff"] = self.object.staff_profile
        context["evaluator"] = self.object.evaluator_name
        return context



"""staff list inside the incharge template """

class InchargeStaffViewPanel(LoginRequiredMixin,ListView):
    model = Employee
    template_name = "nursing_admin/stafflistInsideInchargePage.html"
    context_object_name = "staff_list"

    def get_queryset(self):
        user=self.request.user
        staff_list_orm = Employee.objects.filter(location=user.location)
        return staff_list_orm





class InchargeFormsListView(View):
    template_name = "nursing_admin/form_listing.html"

    def get(self, request):
        # ✅ Filter only forms submitted by the logged-in incharge
        if request.user.is_authenticated and request.user.is_incharge:
            forms = Form1_assement.objects.filter(evaluator_name=request.user).order_by('-evaluation_date')
        else:
            forms = []

        return render(request, self.template_name, {'forms': forms})
    

