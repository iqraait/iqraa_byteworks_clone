from django.urls import path
from .views import NewJoinEmployeeCreate

app_name = 'hr_department'  # Must have this namespace

urlpatterns = [
    path('staff_new_joining/',NewJoinEmployeeCreate.as_view(),name='NewJoiningStaff'),


]