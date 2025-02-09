from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_user(request):
   if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
        # Redirect to a success page.
        ...
      else:
        messages.error(request,("RECHECK IF THE ENTERED USERNAME AAND PASSWORD ARE CORRECT"))
        return redirect('login')
        # Return an 'invalid login' error message.
        ...
       

   # return HttpResponse("<h1>this is home page</h1>")
   else:    
     return render(request ,'login.html')
   
   
   
def logout_user(request):
  logout(request)
  messages.success(request,("you are loged out"))
  return redirect('login')

def register_user(request):
   if request.method == "POST":
     form = UserCreationForm(request.POST)
     if form.is_valid():
       form.save()
       username =form.cleaned_data['username']
       password =form.cleaned_data['password1']
       user = authenticate(username=username, password=password)
       login(request ,user)
       messages.success(request, ("Registration successful"))
       return redirect('home')
     else:
            # Form is not valid, display errors
            messages.error(request, "Error with your form. Please correct the errors.")
            return render(request, 'register.html', {'form': form})
     
   else:
    form=UserCreationForm()
    return render(request ,'register.html',{'form':form,})
