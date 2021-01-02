from django.shortcuts import render, redirect

def register(req):
    return render(req, 'register.html')

def login(req):
    return render(req, 'login.html')

def logout(req):
    return redirect('index.html')

def dashboard(req):
    return render('dashboard.html')
