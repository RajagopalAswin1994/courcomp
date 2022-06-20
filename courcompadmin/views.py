from django.shortcuts import render

# Create your views here.
def courseadmin(request):
    return render(request, 'courcompadmin/index.html')
    
def categories(request):
    return render(request,'courcompadmin/categories.html')