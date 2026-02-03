from django.contrib import admin
from .models import Hr_Department_Main_Model


@admin.register(Hr_Department_Main_Model)
class HrDepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "iqraa_id",
        "email",
        "designation",
        "location",
        "employee_category",
        "mobile_phone",

    )
    list_filter = ("employee_category", "mobile_phone", "location")
    search_fields = ("iqraa_id", "email", "designation", "employee_category", "location")
    ordering = ("-created",)
