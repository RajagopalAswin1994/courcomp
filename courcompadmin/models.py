from email.policy import default
from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Enquiry_DB(models.Model):
    full_name = models.CharField(max_length = 75)
    mobile_number = models.IntegerField()
    email_id = models.EmailField()

class Personal_details(models.Model):
    registration_id = models.CharField(max_length=8,default='NA')
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6,default='NA')
    father_name = models.CharField(max_length=75,default='NA')
    mother_name = models.CharField(max_length=75,default='NA')
    marital_status = models.CharField(max_length=15,default='NA')

class Educational_Details(models.Model):
    registration_id = models.CharField(max_length=8)
    education = models.CharField(max_length=6)
    course = models.CharField(max_length=45)
    specialization = models.CharField(max_length=45)
    university_college = models.CharField(max_length=125)
    course_type = models.CharField(max_length=20)
    passingout_year = models.IntegerField()
    grading_system = models.CharField(max_length=15)
    grading_value = models.FloatField()

class Communication_Details(models.Model):
    registration_id = models.CharField(max_length=8)
    email_id = models.EmailField()
    phone_number_1 = PhoneNumberField()
    phone_number_2 = PhoneNumberField()
    p_address = models.CharField(max_length=125)
    city = models.CharField(max_length=25)
    pincode = models.CharField(max_length=15)
    

class Registration_Details(models.Model):
    registration_id = models.CharField(max_length=8)
    enrollment_date = models.DateField()
    course_enrolled = models.CharField(max_length=8)
    enrollment_institute = models.CharField(max_length=8)

class Course_Categories(models.Model):
    category_name = models.CharField(max_length = 75)
    course_name = models.CharField(max_length = 75)

class Course_Details(models.Model):
    course_id = models.CharField(max_length=8,default='NA') 
    institute_id = models.CharField(max_length=8,default='NA')
    course_name = models.CharField(max_length = 75)
    What_you_learn = models.CharField(max_length=256,default='NA')
    description = models.CharField(max_length=256,default='NA')
    price = models.IntegerField()
    duration = models.IntegerField()
    duration_type = models.CharField(max_length = 75)
    course_through = models.CharField(max_length = 75)
    course_type = models.CharField(max_length = 75)
    course_category = models.CharField(max_length = 75)
    course_banner = models.ImageField(upload_to='uploads')
    

class Company_Details(models.Model):
    institute_id = models.CharField(max_length=8,default='NA')
    comapany_name = models.CharField(max_length = 75)
    courses_provided = models.CharField(max_length = 75)
    phone_number = PhoneNumberField()
    email_id = models.EmailField()
    contact_person = models.CharField(max_length=75,default='not updated')

class Company_Features(models.Model):
    company_name = models.CharField(max_length=75)
    feature_name = models.CharField(max_length=75)
    feature_value = models.CharField(max_length=75)
