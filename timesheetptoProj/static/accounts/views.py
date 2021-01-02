from django.shortcuts import render, redirect
#from django.contrib import messages
#form automatically linked to Auth User model
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.decorators import login_required

#messages.error(req, 'TESTING MESSAGE')

def login(req):
    if req.method == 'POST':
        print('LOGIN POST')
    else:
        pass
    return render(req, 'login.html')

def logout(req):
    return render(req, 'index.html')

def dashboard(req):
    return render(req, 'dashboard.html')
    

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        #get form ready to create new user
        form = UserCreationForm()
    #display the registration form in register.html
    return render(req, 'register.html', {'form': form})


