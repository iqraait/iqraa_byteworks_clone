from django.contrib import admin
from .models import It_Department_Main_model


@admin.register(It_Department_Main_model)
class ItDepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "new_employee",
        "logged_user",
        "is_completed",
        "mail_send",
        "privilege",
        "credentials_setup",
        "whats_app_link",

    )
    list_filter = (
        "is_completed",
        "mail_send",
        "privilege",
        "credentials_setup",
        "whats_app_link",
    )
    search_fields = ("new_employee__id", "logged_user__id")
    ordering = ("-created",)
