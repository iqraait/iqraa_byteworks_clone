from django.db import models
from users.models import BaseModel


MOBILE_CHOICES = (("ANDROID","ANDROID"),
                  ("IPHONE","IPHONE"))

class Hr_Department_Main_Model(BaseModel):
    iqraa_id = models.IntegerField()
    email = models.EmailField(max_length=254,blank=True)
    designation = models.CharField(max_length=254,blank=True)
    location = models.CharField(max_length=254,blank=True)
    employee_category = models.CharField(max_length=254,blank=True)
    mobile_phone = models.CharField(max_length=20,choices=MOBILE_CHOICES)


    def __str__(self):
        return str(self.iqraa_id)




