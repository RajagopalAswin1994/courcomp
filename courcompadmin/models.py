from pyexpat import model
from django.db import models

# Create your models here.
class Enquiry_DB(models.Model):
    full_name = models.CharField(max_length = 75)
    mobile_number = models.IntegerField(max_length= 10)
    email_id = models.EmailField()

class Personal_details(models.Model):
    pass

class Course_Categories(models.Model):
    pass

class Course_Details(models.Model):
    pass

class Educational_Details(models.Model):
    pass

class Communication_Details(models.Model):
    pass

class Registration_Details(models.Model):
    pass