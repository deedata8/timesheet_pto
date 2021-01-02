from django.shortcuts import render, redirect
from django.urls import reverse
#from django.contrib import messages
#Form below automatically linked to Auth User model. Login and Logout are already created by Class Based Views- see urls.py
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.decorators import login_required

#messages.error(req, 'TESTING MESSAGE')

def login(req, context={}):
    # if context != {}:
    #     #display message in login box
    #     return render(req, 'login.html', context)
    if req.method == 'POST':
        print('LOGIN POST')
    else:
        pass
    return render(req, 'registration/login.html')

def logout(req):
    return render(req, 'registration/index.html')

def dashboard(req):
    return render(req, 'dashboard.html')
    

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
            #response = login(req, {'text': 'You are registered. Please sign in.'})
            #return render(req, 'login', {'text': 'You are registered. Please sign in.'})
    else:
        #get form ready to create new user
        form = UserCreationForm()
    #display the registration form in register.html
    return render(req, 'registration/register.html', {'form': form})




