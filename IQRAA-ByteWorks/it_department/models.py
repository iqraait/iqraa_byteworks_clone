from django.db import models
from hr_department.models import Hr_Department_Main_Model
from users.models import BaseModel,Employee


class It_Department_Main_model(BaseModel):
    new_employee = models.ForeignKey(Hr_Department_Main_Model,blank=True,null=True,on_delete=models.SET_NULL)
    logged_user = models.ForeignKey(Employee,blank=True,null=True,on_delete=models.SET_NULL)
    is_completed = models.BooleanField(default=False)
    mail_send = models.BooleanField(default=False)
    privilege = models.BooleanField(default=False)
    credentials_setup = models.BooleanField(default=False)
    whats_app_link = models.BooleanField(default=False)


    def __str__(self):
        return f"The New Employee is {str(self.new_employee)}"
