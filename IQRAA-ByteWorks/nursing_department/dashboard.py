from nursing_department.models import Name_of_Form, Form1_assement
from users.models import Location
from .models import StaffProfile
from nursing_department.selectors import get_dashboard_status

def get_incharge_dashboard_data(employee):
    locations = Location.objects.filter(incharge=employee).only('id') # only filter the id for better sccala
    location_ids = locations.values_list('id', flat=True)  # if incharge have multiple location saves into a tuple


    forms = (
        Name_of_Form.objects
        .filter(location_form__id__in=location_ids)
        .select_related()
        .only('id', 'name', 'describtion', 'created')
        .order_by('-created')
)

    recent_activities = (Form1_assement.objects
                         .filter(evaluator_name=employee)
                         .select_related('form_name')
                         .order_by('-updated')[:2])

    staff_list = (StaffProfile.objects
                  .filter(employee__location__incharge=employee)   # also for needed data
                  .only('staff_name', 'employee'))

    status = get_dashboard_status(employee) if employee else {
        "total_forms": 0,
        "pending_forms": 0,
        "approved_forms": 0,
        "average_score": 0
    }

    return {
        "forms": forms,
        "recent_activities": recent_activities,
        "staff_list": staff_list,
        "status": status
    }

