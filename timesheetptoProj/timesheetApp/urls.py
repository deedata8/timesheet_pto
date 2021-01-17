from django.urls import path
from . import views

app_name = 'timesheetApp'

urlpatterns = [
    #timesheet homepage
    path('', views.index, name='timesheet-index'),
    #go to template for data entry- calendar and timesheet
    path('entry/', views.entry, name='set-date'),
    #not a new template, get data to populate date fields
    path('timesheet/', views.get_timesheet, name='timesheet-entry'),
    #redirect after submitting timesheet
    path('pto-summary/', views.pto_summary, name='pto-summary'),
]