"""courcomp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from courcomphome import views as sitehome
from courcompadmin import views as siteadmin 
from courcompadmin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sitehome.home),
    path('courselist',sitehome.courselist),
    path('courcompadmin/',siteadmin.courseadmin),
    path('categories/',siteadmin.categories),
    path('dashboard/',siteadmin.dashboard),
    path('companies/',siteadmin.companies),
    path('courses/',siteadmin.courses),
    path('enquiry/',siteadmin.enquiry),
    path('enrollments/',siteadmin.enrollments)
    
]
