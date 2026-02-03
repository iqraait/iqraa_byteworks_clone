from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Employee, Department, Location

class EmployeeChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee

class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = ('iqraa_id', 'department')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name',)
    search_fields = ('department_name',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name',)
    search_fields = ('location_name',)
    list_filter = ('department_of_location',)



class EmployeeAdmin(UserAdmin):
    form = EmployeeChangeForm
    add_form = EmployeeCreationForm
    
    # Admin list view
    list_display = ('iqraa_id', 'username','location', 'is_incharge', 'is_staff_nurse','is_superint', 'created')
    list_filter = ('iqraa_id','department', 'is_staff_nurse', 'is_superuser')
    list_editable = ('is_incharge', 'is_staff_nurse')
    
    # Fields organization in edit view
    fieldsets = (
        (None, {'fields': ('iqraa_id', 'password')}),
        ('Personal Info', {'fields': ('username','department','location')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff_nurse', 'is_superuser', 
                      'groups', 'user_permissions','is_incharge','is_superint'),
        }),
        ('Important Dates', {'fields': ('last_login', 'created', 'updated')}),
    )
    
    # Fields for add/create view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('iqraa_id', 'department', 'password1', 'password2','location'),
        }),
    )
    
    # Search and ordering
    search_fields = ('iqraa_id',)
    ordering = ('-created',)
    list_filter = ('location', 'is_staff_nurse', 'is_incharge')
    filter_horizontal = ('groups', 'user_permissions',)
    
    # Timestamp and soft-delete handling
    readonly_fields = ('created', 'updated', 'last_login')
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(soft_delete=False)



# Register models
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Location,LocationAdmin)




