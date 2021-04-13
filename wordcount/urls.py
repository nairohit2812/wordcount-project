"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
#views is the 1st file created for navigation


urlpatterns = [
    path('', views.homepage),
    path('count/',views.count, name = 'count'),
    path('about/',views.about, name = 'about'),
#name = count is from the hhome.html's form action name    
#    path('admin/', admin.site.urls),   
#this is the default path cretaed which lands onto the django webpage. 
]
