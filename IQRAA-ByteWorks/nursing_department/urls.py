# from django.urls import path
# from .views import (InchargeDashboard,
#                     AdminDashboardView,
#                     PreviewForm,
#                     AdminDashboardView,
#                     ApproveAssementView,
#                 #     StaffRegistrationView,
#                     AssmentDetailedView,
#                     InchargeFormsListView,
#                     StaffFormsView,
#                 #     ApproveStaffFormView,
#                         InchargeStaffViewPanel,
#                     StaffApproveAssementView,
#                     Form1AssessmentDetailView
#                     )

# app_name = 'nursing_department'  # Must have this namespace




# urlpatterns = [

#         path('InchargeDashboard',InchargeDashboard.as_view(),name='InchargeDashboard'),
#         path('NicuAssementForm/',PreviewForm.as_view(),name="nicuform"),
#         path("admin_dashboard/", AdminDashboardView.as_view(), name="nursing_admin_dashboard"),
#         path("assessment/<int:pk>/", AssmentDetailedView.as_view(), name="assessment_detail"),
#         path("approve/<int:pk>/", ApproveAssementView.as_view(), name="approve_assessment"),
#         path("staff-approve/<int:pk>/", StaffApproveAssementView.as_view(), name="staff_approve_assessment"),
#         # path('staff-register/', StaffRegistrationView.as_view(), name='staff_register'),
#         path('formslisting',InchargeFormsListView.as_view(),name="InchargeForms"),
#         path('my-forms/', StaffFormsView.as_view(), name='my_forms'),
#         # path('approve-form/<int:pk>/', ApproveStaffFormView.as_view(), name='approve_form'),
#         path('assessment/<int:pk>/view/', Form1AssessmentDetailView.as_view(), name='form1_view'),
#         path('stafflist-incharge',InchargeStaffViewPanel.as_view(),name='InchargeStaffViewList')


        




# ]
from django.urls import path
from .views import (InchargeDashboard,
                    AdminDashboardView,
                    WardAssementForm,
                    AdminDashboardView,
                    ApproveAssementView,
                #     StaffRegistrationView,
                    AssmentDetailedView,
                    InchargeFormsListView,
                    StaffFormsView,
                #     ApproveStaffFormView,
                        InchargeStaffViewPanel,
                    StaffApproveAssementView,
                    Form1AssessmentDetailView
                    )

app_name = 'nursing_department'  # Must have this namespace




urlpatterns = [

        path('InchargeDashboard/',InchargeDashboard.as_view(),name='InchargeDashboard'),
        path('WardAssmentForm/',WardAssementForm.as_view(),name="wardassmentform"),
        path("admin_dashboard/", AdminDashboardView.as_view(), name="nursing_admin_dashboard"),
        path("assessment/<int:pk>/", AssmentDetailedView.as_view(), name="assessment_detail"),
        path("approve/<int:pk>/", ApproveAssementView.as_view(), name="approve_assessment"),
        path("staff-approve/<int:pk>/", StaffApproveAssementView.as_view(), name="staff_approve_assessment"),
        # path('staff-register/', StaffRegistrationView.as_view(), name='staff_register'),
        path('formslisting',InchargeFormsListView.as_view(),name="InchargeForms"),
        path('my-forms/', StaffFormsView.as_view(), name='my_forms'),
        # path('approve-form/<int:pk>/', ApproveStaffFormView.as_view(), name='approve_form'),
        path('assessment/<int:pk>/view/', Form1AssessmentDetailView.as_view(), name='form1_view'),
        path('stafflist-incharge',InchargeStaffViewPanel.as_view(),name='InchargeStaffViewList')


        




]
