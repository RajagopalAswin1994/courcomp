from django.shortcuts import render,redirect
from courcompadmin.models import *
from courcompadmin.forms import *

# Create your views here.
def courseadmin(request):
    return render(request, 'courcompadmin/index.html')
    
def categories(request):    
    CourseCategories = Course_Categories.objects.all()
    CourseCategoriesForm = Course_Categories_Form()
    if request.method == 'POST':
        form = Course_Categories_Form(request.POST)
        if form.is_valid():
            form.save()            
            return render(request,'courcompadmin/categories.html',{'coursecategories':CourseCategories,'coursecategoriesform':CourseCategoriesForm})   
    else:                  
        return render(request,'courcompadmin/categories.html',{'coursecategories':CourseCategories,'coursecategoriesform':CourseCategoriesForm})  

def dashboard(request):
    return render(request,'courcompadmin/dashboard.html')

def companies(request):
    Companies = Company_Details.objects.all()
    CompaniesForm = Company_Details_Form()
    if request.method == 'POST':
        form = Company_Details_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'courcompadmin/companies.html',{'companies':Companies,'companyform':CompaniesForm})
    else:                  
        return render(request,'courcompadmin/companies.html',{'companies':Companies,'companyform':CompaniesForm})
   

def courses(request,*args, **kwargs):
    Courses = Course_Details.objects.all()   
    if request.method == 'POST':
        course_form = Course_Details_Form()
        form = Course_Details_Form(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return render(request,'courcompadmin/courses.html',{'courses':Courses,'course_form':course_form})
    else:
        course_form = Course_Details_Form()
        return render(request,'courcompadmin/courses.html',{'courses':Courses,'course_form':course_form})
        
    
def enquiry(request):
    Enquires = Enquiry_DB.objects.all()    
    return render(request,'courcompadmin/enquiry.html',{'Enquires':Enquires})

def enrollments(request):
    return render(request,'courcompadmin/enrollments.html')