from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
class CustomUser(AbstractUser):
    reg = RegexValidator(r'^[+]{0,1}[0-9]{10,12}','Invalid Mobile Number')
    phone = models.CharField(max_length=13, validators=[reg])
    email = models.EmailField(unique=True, blank=False)
    institute = models.CharField(max_length=40)
    dob = models.DateField(null=True)
    
