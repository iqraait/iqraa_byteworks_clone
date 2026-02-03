from .models import Employee,Form1_assement


class StaffAdminServices:
    def ActiveUser(self):
        active_user = Employee.objects.filter(is_active=True).count()
        return active_user

    def PendingForms(self):
        pending_forms = Form1_assement.objects.filter(is_approved=False).count()