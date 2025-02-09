from django.urls import path
from home import views
#first it will go to urls.py of multipledisese from there it will go to url.py of home
#from ther it will go to views .py of home 
#we use the migrate function when we make some model and we need to perform operation on it via database 
urlpatterns = [

    
    path('home',views.index,name='home'),
    path('about', views.about ,name='about'),
    path('contact', views.contact ,name='contact'),
    path('diabetesprediction', views.diabetesprediction ,name='diabetesprediction'),
    path('parkinsons', views.parkinsons ,name='parkinsons'),
    path('breastcancer', views.breastcancer ,name='breastcancer'),
    path('cardiovascular', views.cardiovascular ,name='cardiovascular'),
   
    


]
