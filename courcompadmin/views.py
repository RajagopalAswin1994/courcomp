from django.shortcuts import render

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