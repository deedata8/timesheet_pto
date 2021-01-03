from django.db import models
from datetime import datetime
#from django.contrib.auth.models import User
from django.conf import settings

class Timesheet(models.Model):
    #employee = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    #employee_id = models.CharField(max_length=200)
    hire_date = models.DateField(null=True) 
    timesheet_stamp = models.DateTimeField(default=datetime.now) 
    timesheet_date = models.DateField(null=True) 
    day_worked_hours = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    

