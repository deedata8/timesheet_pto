from django.urls import path
from . import views

app_name = 'timesheetApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('entry/', views.entry, name='set-date'),
    path('timesheet/', views.get_timesheet, name='timesheet-entry'),
    path('timesheet-review/', views.timesheet_review, name='timesheet-review'),
    path('pto-summary/', views.pto_summary, name='pto-summary'),
]