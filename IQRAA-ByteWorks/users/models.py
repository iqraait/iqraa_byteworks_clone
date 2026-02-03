from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager



"""Base model Database"""
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True 


"""Data-base table for the Departments"""


class Department(BaseModel):
    department_name = models.CharField(max_length=30)
    incharges = models.ManyToManyField(
        'Employee',
        blank=True,
        related_name='secondary_incharge_of'
    )
 

    def __str__(self):
        return self.department_name



class Location(BaseModel):
    location_name = models.CharField(max_length=100,unique=True)
    department_of_location = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    form_name = models.ForeignKey(
        'nursing_department.Name_of_Form',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='location_form',
    )
    incharge = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True,related_name='departments_incharge_of' )


    def __str__(self):
        return self.location_name



"""custom User_Manager code"""



class EmployeeManager(BaseUserManager):
    def create_user(self, iqraa_id,  password=None, **extra_fields):
        if not iqraa_id:
            raise ValueError("Users must have an Iqraa ID")
        
        user = self.model(
            iqraa_id=iqraa_id,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, iqraa_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user(iqraa_id, password, **extra_fields)
    


"""Data_model for the Employee"""



class Employee(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=100,blank=True,null=True)

    iqraa_id = models.CharField(unique=True, null=False, blank=False)

    password = models.CharField(max_length=128)

    is_incharge = models.BooleanField(default=False,
                                      help_text="Incharge Designation")
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site."
    )
    is_superuser = models.BooleanField(
        default=False,
        help_text="Designates that this user has all permissions without explicitly assigning them."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Designates whether this user should be treated as active."
    )    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True,related_name='employees')

    location = models.ForeignKey(Location,on_delete=models.SET_NULL,blank=True,null=True)

    is_superint = models.BooleanField(default=False,help_text="nursing_superient")

    is_staff_nurse = models.BooleanField(default=False,help_text="for normal nursing staff")



    USERNAME_FIELD = 'iqraa_id'
    REQUIRED_FIELDS = []

    objects = EmployeeManager()




    def __str__(self):
        return str(self.iqraa_id)
    

