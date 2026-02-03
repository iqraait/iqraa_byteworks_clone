
from django.db import models
from users.models import BaseModel,Employee,Location
from django.db.models import JSONField  # Django ≥ 3.1
from django.core.validators import MinValueValidator, MaxValueValidator
from .constants_data import EVALUATION_PERFOMANCE
from datetime import datetime




class Name_of_Form(BaseModel):
    name =  models.CharField(max_length=100,blank=True,null=True)
    describtion = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.name



class Evalution_period(BaseModel):
    evaluation_period = models.CharField(max_length=100, blank=False, null=False, help_text="Evaluation period of the assessment")

    def __str__(self):
        return self.evaluation_period
    


class StaffProfile(BaseModel):
    DESIGNATION_CHOICES = [
        ('NURSING_OFFICER', 'Nursing Officer'),
        ('SENIOR_NURSING_OFFICER', 'Senior Nursing Officer'),
        ('NURSING_AID', 'Nursing AID'),
    ]

    employee = models.ForeignKey(Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profile_employee"
    )
    designation = models.CharField(
        max_length=150,
        choices=DESIGNATION_CHOICES,
        default='NURSING_OFFICER'
    )
    date_of_join = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.employee}"




class Form1_assement(BaseModel):

    staff_profile = models.ForeignKey(
        StaffProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assessments"

)



    evaluation_period = models.ForeignKey(
        Evalution_period,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="assessments"
    )


        
    evaluator_name = models.ForeignKey('users.Employee',on_delete=models.SET_NULL,blank=True,null=True)
    

    total_score = models.IntegerField(null=True,blank=True)

    percentage = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0), MaxValueValidator(100)])

    data = JSONField(default=dict)

    evaluation_date = models.DateField(auto_now_add=True)

    approved_evalutor_id = models.CharField(max_length=6,blank=True,null=True)

    is_approved = models.BooleanField(default=False)

    form_name = models.ForeignKey(Name_of_Form,on_delete=models.SET_NULL, null=True,blank=True)

    staff_acknowdged = models.BooleanField(default=False)

    evaluation_year = models.IntegerField(default=datetime.now().year)




    class Meta:
        unique_together = ('staff_profile', 'evaluation_period')
        ordering = ['-evaluation_date']
                

    # def __str__(self):
    #     staff = str(self.staff_profile) if self.staff_profile else "No Staff"
    #     period = self.evaluation_period.evaluation_period if self.evaluation_period else "No Period"
    #     return f"{self.staff_profile} - {period}"
                