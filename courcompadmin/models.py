from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Enquiry_DB(models.Model):
    full_name = models.CharField(max_length = 75)
    mobile_number = models.IntegerField()
    email_id = models.EmailField()

class Personal_details(models.Model):
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    date_of_birth = models.DateField()

# class Educational_Details(models.Model):
#     pass

# class Communication_Details(models.Model):
#     pass

# class Registration_Details(models.Model):
#     pass

class Course_Categories(models.Model):
    category_name = models.CharField(max_length = 75)
    course_name = models.CharField(max_length = 75)

class Course_Details(models.Model):
    course_name = models.CharField(max_length = 75)
    price = models.IntegerField()
    duration = models.IntegerField()
    duration_type = models.CharField(max_length = 75)
    course_through = models.CharField(max_length = 75)
    course_type = models.CharField(max_length = 75)
    course_category = models.CharField(max_length = 75)

class Company_Details(models.Model):
    comapany_name = models.CharField(max_length = 75)
    courses_provided = models.CharField(max_length = 75)
    phone_number = PhoneNumberField()
    email_id = models.EmailField()
    contact_person = models.CharField(max_length=75,default='not updated')

class Company_Features(models.Model):
    company_name = models.CharField(max_length=75)
    feature_name = models.CharField(max_length=75)
    feature_value = models.CharField(max_length=75)