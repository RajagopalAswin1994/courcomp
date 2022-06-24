import email
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','courcomp.settings')

import django
django.setup()

from courcompadmin.models import *
from faker import Faker
from random import *
import random

faker = Faker()
courses_list =['Python','Java','Data Science','Business Intelligence','Data Analytics','Django']
def Gen_Enquiry(n):
    for i in range(n):
        f_full_name = faker.name()
        f_mobile_number = faker.phone_number()
        f_email_id = f_full_name + '@gmail.com'
        Enquiry_data = Enquiry_DB.objects.get_or_create(full_name = f_full_name,mobile_number = f_mobile_number, email_id = f_email_id)

def Gen_Company(n):
    for i in range(n):         
        f_comapany_name = faker.company()
        f_courses_provided = random.choice(courses_list)
        f_phone_number = faker.phone_number()
        f_email_id = faker.ascii_free_email()
        Company_data = Company_Details.objects.get_or_create(comapany_name = f_comapany_name,courses_provided = f_courses_provided,phone_number = f_phone_number,email_id = f_email_id)


Gen_Company(20)