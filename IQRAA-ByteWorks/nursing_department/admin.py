from django.contrib import admin
from .models import StaffProfile, Form1_assement, Name_of_Form, Evalution_period


@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ("employee", "designation", "date_of_join")
    search_fields = ("employee", "designation", "employee__iqraa_id")
    list_filter = ("designation",)


@admin.register(Name_of_Form)
class NameOfFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'describtion', 'created')
    search_fields = ('name',)


@admin.register(Evalution_period)
class EvaluationPeriodAdmin(admin.ModelAdmin):
    list_display = ('evaluation_period', 'created')
    search_fields = ('evaluation_period',)


@admin.register(Form1_assement)
class Form1AssessmentAdmin(admin.ModelAdmin):
    list_display = (
        'staff_profile',
        'evaluation_period',
        'evaluator_name',
        'total_score',
        'percentage',
        'evaluation_date',
        'is_approved',
        'staff_acknowdged',
        'form_name',
    )
    list_filter = ('evaluation_period', 'evaluation_date', 'is_approved')
    search_fields = ('staff_profile', 'evaluator_name')
    date_hierarchy = 'evaluation_date'
    ordering = ('-evaluation_date',)
    raw_id_fields = ('staff_profile',  'form_name', 'evaluation_period')

    fieldsets = (
        ('Basic Information', {
            'fields': ('staff_profile',  'evaluation_period', 'form_name','evaluation_year')
        }),
        ('Evaluation Details', {
            'fields': ('evaluator_name', 'total_score', 'percentage', 'data')
        }),
        ('Approval Info', {
            'fields': ('is_approved', 'staff_acknowdged', 'approved_evalutor_id')
        }),
    )
