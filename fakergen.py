import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','courcomp.settings')

import django
django.setup()

from courcompadmin.models import *
from faker import Faker
from random import *
faker = Faker()

def Gen_Enquiry(n):
    for i in range(n):
        f_full_name = faker.name()
        f_mobile_number = randint(1111111111,9999999999)
        f_email_id = f_full_name + '@gmail.com'
        Enquiry_data = Enquiry_DB.objects.get_or_create(full_name = f_full_name,mobile_number = f_mobile_number, email_id = f_email_id)


Gen_Enquiry(200)