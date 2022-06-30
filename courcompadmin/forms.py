from django import forms
from courcompadmin.models import *

class Course_Details_Form(forms.ModelForm):
    
    class Meta:
        model = Course_Details
        fields = "__all__"
