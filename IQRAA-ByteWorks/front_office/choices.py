from django.db import models


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    UNDERTERMINED = 'O', 'Undertermined'
    TRANSGENDER = 'T', 'Transgender'

class Patient_type(models.TextChoices):
    GENERAL = 'G','General'
    CAMP = 'C','Camp'
    CARD_HOLDER = 'CH','Card Holder'
    CORPORATE = 'CO','Corporate'
    CARDLE = 'CA','Cardle'
    EMPLOYEE = 'EM','Employee'
    ESI = 'ES', 'ESI'

class Title(models.TextChoices):
    MR = 'MR','Mr'
    MRS = 'MRS','MRS'
    MISS = 'MISS', 'Miss'  
    PROF = 'PROF', 'Professor'  
    MSTR = "MSTR", "Mstr"
    DR = "DR","DR"
    
class Visit(models.TextChoices):
    MORNING = 'MRNG','Morning'
    EVENING = 'EVNG',"Evening"

class Registration_type(models.TextChoices):
    TOKEN = "Tk","Token"
    BOOKING = "BK","Booking"
    NEW_TOKEN  = "NK", "New Token"
    


class City(models.TextChoices):
    THIRUVANANTHAPURAM = "TVM", "Thiruvananthapuram"
    KOLLAM = "KLMM", "Kollam"
    PATHANAMTHITTA = "PTA", "Pathanamthitta"
    ALAPPUZHA = "ALP", "Alappuzha"
    KOTTAYAM = "KTM", "Kottayam"
    IDUKKI = "IDK", "Idukki"
    ERNAKULAM = "EKM", "Ernakulam"
    THRISSUR = "TSR", "Thrissur"
    PALAKKAD = "PLK", "Palakkad"
    MALAPPURAM = "MLP", "Malappuram"
    KOZHIKODE = "KKD", "Kozhikode"
    WAYANAD = "WYD", "Wayanad"
    KANNUR = "KNR", "Kannur"
    KASARAGOD = "KGD", "Kasaragod"


class State(models.TextChoices):
    KERALA = "KL","Kerala"


class RegistrationType(models.TextChoices):
    TOKEN = "token", "Token"
    BOOKING = "booking", "Booking"
    NEW_TOKEN = "new_token", "New Token"

