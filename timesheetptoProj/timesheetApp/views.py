from django.shortcuts import render

def index(req):
    return render(req, 'index_timesheet.html')
