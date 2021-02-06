from django.db import models

# Create your models here.
class Books(models.Model):
    Not_Selected = 'NULL'
    Basic_Electrical_Engineering = 'EE_101'
    Engineering_Mathematics1 = 'MA_111'     
    Comunnication_Skills ='HS_101'
    Engineering_Workshop ='ME_102'
    Engineering_Chemistry ='CY_101'
    Materials_Science = 'MS_101'
    Computer_Programming = 'CS_101'
    Engineering_Graphics = 'ME_101'
    Engineering_Physics = 'PH_101'
    Applied_Mechanics = 'PH_101'
    Basic_Electronics_Engineering = 'EC_101'
    Engineering_Mathematics2 = 'MA_121'
    Subs=[ 
        (Not_Selected, 'Not Declared'),
        (Basic_Electrical_Engineering, 'Basic Electrical Enginering'),
        (Engineering_Mathematics1, 'Engineering Maths1'),
        (Comunnication_Skills, 'Communication Skills'),
        (Engineering_Workshop,'Engineering Workshop'),
        (Engineering_Chemistry,'Engineering Chemistry'),
        (Materials_Science,'Materials Science '),
        (Computer_Programming,'Computer Programming'),
        (Engineering_Graphics,'Engineering Graphics'),
        (Engineering_Physics,'Engineering Physics'),
        (Applied_Mechanics,'Applied Mechanics'),
        (Basic_Electronics_Engineering,'Basic Electronics Engineering'),
        (Engineering_Mathematics2,'Engineering Mathematics2')
        ] 
    Name_of_book = models.CharField(max_length=100)
    Author_of_book = models.CharField(max_length=100)
    Subjects = models.CharField(
        max_length=6,
        choices=Subs,
        default=Not_Selected,
        )