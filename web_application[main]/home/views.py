from django.shortcuts import render,HttpResponse
import joblib
import numpy as np
import tensorflow 
import tensorflow as tf
from tensorflow.keras.models import load_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


model1 = load_model('static/breastmodel1.keras')
model = joblib.load('static/diabetes_model')
model2=joblib.load('static/heart_model1')
model3=joblib.load('static/parkinson_model')

# Create your views here.
def index(request):
   # return HttpResponse("<h1>this is home page</h1>")
    return render(request ,'index.html')

def contact(request):
   # return HttpResponse("<h1>this is contact page</h1>")
    return render(request ,'contact.html')





def about(request):
   # return HttpResponse("<h1>this is about page</h1>")
    return render(request ,'about.html')

def diabetesprediction(request):
    if request.method == "POST": 
        noofpregnancies = int(request.POST.get('pregnancies'))
        glucose = int(request.POST.get('glucose'))
        bloodpressure = int(request.POST.get('blood pressure'))
        skinthickness = int(request.POST.get('skin thickness'))
        insulin = int(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        diabetespedigreefun = float(request.POST.get('diabetespedigreefun'))
       # diabetepedigreefun = float(diabetespedigreefun)
        age = int(request.POST.get('age'))

        input_data = (noofpregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefun,age)#tupple 

# changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data_reshaped)
        if(prediction[0] == 0):
               pred='The person is not diabetic'
        else:
                pred ='The person is diabetic. They may be prone to other diseases such as hypertension and cardiovascular diseases.'

        return_obj={
             "output":pred
             
        }
        return render(request ,'diabetesprediction.html',return_obj) 

    else:
# return HttpResponse("<h1>this is home page</h1>")
         return render(request ,'diabetesprediction.html')

def parkinsons(request):
   # return HttpResponse("<h1>this is home page</h1>")
    if request.method == "POST": 
        a1 = float(request.POST.get('a1'))
        b1 = float(request.POST.get('b1'))
        c1 =float(request.POST.get('c1'))
        d1 =float(request.POST.get('d1'))
        e1 =float(request.POST.get('e1'))
        f1 = float(request.POST.get('f1'))
        g1 = float(request.POST.get('g1'))
        h1 = float(request.POST.get('h1'))
        i1 =float(request.POST.get('i1'))
        j1 = float(request.POST.get('j1'))
        k1 =float(request.POST.get('k1'))
        l1 = float(request.POST.get('l1'))
        m1 = float(request.POST.get('m1'))
        n1 = float(request.POST.get('n1'))
        o1 = float(request.POST.get('o1'))
        p1 = float(request.POST.get('p1'))
        q1 = float(request.POST.get('q1'))
        r1 = float(request.POST.get('r1'))
        s1 = float(request.POST.get('s1'))
        t1 = float(request.POST.get('t1'))
        u1 = float(request.POST.get('u1'))
        v1 = float(request.POST.get('v1'))


        input_data0 = (a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,u1,v1)
        print(input_data0)
        

# changing the input_data to numpy array
        input_data_as_numpy_array0 = np.asarray(input_data0)

# reshape the array as we are predicting for one instance
        input_data_reshaped0 = input_data_as_numpy_array0.reshape(1,-1)

        prediction0 = model3.predict(input_data_reshaped0)
        
        if(prediction0[0] == 0):
               pred0='The Person does not have Parkinsons Disease'
        else:
                pred0 ='The Person has Parkinsons'

        return_obj0={
             "output1":pred0
             
        }
        return render(request ,'parkinsons.html',return_obj0) 

    else:
# return HttpResponse("<h1>this is home page</h1>")
         return render(request ,'parkinsons.html')

def cardiovascular(request):
    if request.method == "POST": 
        a1 = int(request.POST.get('a1'))
        b1 = int(request.POST.get('b1'))
        c1 = int(request.POST.get('c1'))
        d1 = int(request.POST.get('d1'))
        e1 = int(request.POST.get('e1'))
        f1 = int(request.POST.get('f1'))
        g1 = int(request.POST.get('g1'))
        h1 = int(request.POST.get('h1'))
        i1 = int(request.POST.get('i1'))
        j1 = float(request.POST.get('j1'))
        k1 = int(request.POST.get('k1'))
        l1 = int(request.POST.get('l1'))
        m1 = int(request.POST.get('m1'))

        input_data0 = (a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1)
        

# changing the input_data to numpy array
        input_data_as_numpy_array0 = np.asarray(input_data0)

# reshape the array as we are predicting for one instance
        input_data_reshaped0 = input_data_as_numpy_array0.reshape(1,-1)

        prediction0 = model2.predict(input_data_reshaped0)
        
        if(prediction0[0] == 0):
               pred0='The Person is not prone to a Heart Disease'
        else:
                pred0 ='The Person is prone to a Heart Disease'

        return_obj0={
             "output0":pred0
             
        }
        return render(request ,'cardiovascular.html',return_obj0) 

    else:
# return HttpResponse("<h1>this is home page</h1>")
         return render(request ,'cardiovascular.html')
   # return HttpResponse("<h1>this is home page</h1>")
    

def breastcancer(request):
   # return HttpResponse("<h1>this is home page</h1>")
    if request.method == "POST":
        
        a = float(request.POST.get('awer'))
        b = float(request.POST.get('b'))
        c = float(request.POST.get('c'))
        d = float(request.POST.get('d'))
        e = float(request.POST.get('e'))
        f = float(request.POST.get('f'))
        g = float(request.POST.get('g'))
        h = float(request.POST.get('h'))
        i = float(request.POST.get('i'))
        j = float(request.POST.get('j'))
        k = float(request.POST.get('k'))
        l = float(request.POST.get('l'))
        m = float(request.POST.get('m'))
        n = float(request.POST.get('n'))
        o = float(request.POST.get('o'))
        p = float(request.POST.get('p'))
        q = float(request.POST.get('q'))
        

        input_data1 = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q)
        print(input_data1)

# changing the input_data to numpy array
        input_data_as_numpy_array1 = np.asarray(input_data1)

# reshape the array as we are predicting for one instance
        input_data_reshaped1 = input_data_as_numpy_array1.reshape(1,-1)

        prediction1 = model1.predict(input_data_reshaped1)
        prediction_label = [np.argmax(prediction1)]
        if (prediction_label[0] == 0):
               pred1='The tumor is Malignant'
        else:
                pred1 ='The tumor is Benign'

        return_obj1={
             "output1":pred1
             
        }
        return render(request ,'breastcancer.html',return_obj1) 
    
    else:
        
         return render(request ,'breastcancer.html')

