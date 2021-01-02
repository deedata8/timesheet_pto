from django.shortcuts import render, redirect

def register(req):
    if req.method == 'POST':
        print('REGISTER POST')
    else:
        pass
    return render(req, 'register.html')

def login(req):
    if req.method == 'POST':
        print('LOGIN POST')
    else:
        pass
    return render(req, 'login.html')

def logout(req):
    return redirect('index.html')

def dashboard(req):
    return render('dashboard.html')
