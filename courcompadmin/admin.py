from django.contrib import admin
from courcompadmin.models import Enquiry_DB

# Register your models here.

class Enquiry_Admin(admin.ModelAdmin):
    list_display = ['full_name','mobile_number','email_id']

admin.site.register(Enquiry_DB, Enquiry_Admin)
