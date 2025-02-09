"""
URL configuration for multiplediseaseprediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

#when open the website first the urls.py of project i.e urls.py of multipledisease prediction is opened then 
#it checks if admin then it routs to admin otherwise to home.urls then when we go to url.py of home from there if nothing then we go to the views.py 
#and in views.py  we go to particular funtion we need  
#if we are on the admin page then we will go in admin page if there is nothing then we will go in home.urls  as shown below
#in base.html we will write the code which is common for all pages like header ,footer
#to make any changes to the website we will genrally make changes in views.py because at the end we go there only
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('',include('members.urls'))

]
