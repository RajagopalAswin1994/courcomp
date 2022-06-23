from django.shortcuts import render
from courcompadmin.models import Enquiry_DB

# Create your views here.
def courseadmin(request):
    return render(request, 'courcompadmin/index.html')
    
def categories(request):
    return render(request,'courcompadmin/categories.html')

def dashboard(request):
    return render(request,'courcompadmin/dashboard.html')

def companies(request):
    return render(request,'courcompadmin/companies.html')

def courses(request):
    return render(request,'courcompadmin/courses.html')

def enquiry(request):
    Enquires = Enquiry_DB.objects.all()    
    return render(request,'courcompadmin/enquiry.html',{'Enquires':Enquires})

def enrollments(request):
    return render(request,'courcompadmin/enrollments.html')