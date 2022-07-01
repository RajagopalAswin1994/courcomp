from attr import attr, attrs
from django import forms
from matplotlib import widgets
from courcompadmin.models import *

class Course_Details_Form(forms.ModelForm):
    
    class Meta:
        model = Course_Details
        fields = "__all__"
        widgets = {
            'course_id': forms.TextInput(attrs={'class':'form-control'}),
            'institute_id': forms.ChoiceField(attrs={'class':'form-control'}),
            'course_name': forms.TextInput(attrs={'class':'form-control'}),
            'What_you_learn': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.IntegerField(attrs={'class':'form-control'}),
            'duration': forms.TextInput(attrs={'class':'form-control'}),
            'duration_type': forms.TextInput(attrs={'class':'form-control'}),
            'course_through': forms.TextInput(attrs={'class':'form-control'}),
            'course_type': forms.TextInput(attrs={'class':'form-control'}),
            'course_category': forms.TextInput(attrs={'class':'form-control'})
            # 'course_banner': forms.ImageField(attrs={'class':'form-control'})
        }        