from django.contrib import admin
from courcompadmin.models import *

# Register your models here.

class Enquiry_Admin(admin.ModelAdmin):
    list_display = ['full_name','mobile_number','email_id']

class Course_Categories_Admin(admin.ModelAdmin):
   list_display = ['category_name','course_name']

class Course_Details_Admin(admin.ModelAdmin):
    list_display = ['course_id', 'institute_id', 'course_name', 'What_you_learn', 'description', 'price', 'duration', 'duration_type', 'course_through', 'course_type', 'course_category','course_banner' ]

class Company_Details_Admin(admin.ModelAdmin):
    list_display = ['comapany_name','courses_provided','phone_number','email_id','contact_person']


admin.site.register(Enquiry_DB, Enquiry_Admin)
admin.site.register(Course_Categories, Course_Categories_Admin)
admin.site.register(Course_Details, Course_Details_Admin)
admin.site.register(Company_Details, Company_Details_Admin)
