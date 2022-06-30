from django.shortcuts import render
from courcompadmin.models import *
from courcompadmin.forms import *

# Create your views here.
def courseadmin(request):
    return render(request, 'courcompadmin/index.html')
    
def categories(request):
    CourseCategories = Course_Categories.objects.all()    
    return render(request,'courcompadmin/categories.html',{'CourseCategories':CourseCategories})

def dashboard(request):
    return render(request,'courcompadmin/dashboard.html')

def companies(request):
    Companies = Company_Details.objects.all()
    return render(request,'courcompadmin/companies.html',{'companies':Companies})

def courses(request):
    # Courses = Company_Details.objects.all()'courses':Courses,
    course_form = Course_Details_Form()
    return render(request,'courcompadmin/courses.html',{'course_form':course_form})

def enquiry(request):
    Enquires = Enquiry_DB.objects.all()    
    return render(request,'courcompadmin/enquiry.html',{'Enquires':Enquires})

def enrollments(request):
    return render(request,'courcompadmin/enrollments.html')