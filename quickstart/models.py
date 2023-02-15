from django.db import models

# Create your models here.

class Students(models.Model):
    GENDERCHOICE = (
        ('male', 'male'),
        ('female', 'female'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDERCHOICE)
    age = models.IntegerField()