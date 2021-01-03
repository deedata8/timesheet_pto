from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .calcs import get_week
from .models import Timesheet


def index(req):
    return render(req, 'index_timesheet.html')

@login_required
def entry(req):
    return render(req, 'set_date.html')

@login_required
def get_timesheet(req):
    input = str(req.GET["date"])
    if input != '':
        #get current week's timesheet header dates and days
        wkdy_list, md_list = get_week(input)
    else:
        return render(req, 'set_date.html')

    return render(req, 'set_date.html', 
        {'weekday_list': wkdy_list, 'month_day_list': md_list})


#display timesheet for review and submit [to admin] for approval
@login_required
def timesheet_review(req):
    #headers
    md_list = req.POST.getlist("month_day_list")
    wkdy_list = req.POST.getlist("weekday_list")
    #hours
    wk_hrs_list = req.POST.getlist("hrs_worked")
    pto_hrs_list = req.POST.getlist("hrs_pto")
    wk_hrs_list = [float(hr) for hr in wk_hrs_list]
    pto_hrs_list = [float(hr) for hr in pto_hrs_list]
    tot_wk_hrs = sum(wk_hrs_list)
    tot_pto_hrs = sum(pto_hrs_list)

    return render(req, 'confirm_entry.html', 
        {'wk_hrs': wk_hrs_list, 'pto_hrs': pto_hrs_list, 
            'tot_wk_hrs': tot_wk_hrs, 'tot_pto_hrs': tot_pto_hrs,
            'weekday_list': wkdy_list, 'month_day_list': md_list})


@login_required
#def pto_summary(req, md_list, wk_hrs_list, pto_hrs_list, tot_wk_hrs, tot_pto_hrs):
def pto_summary(req):
    user = req.user
    userObj = User.objects.get(id=user.id)
    md_list = req.POST.getlist("wk_hrs_list")
    print('=====================')
    print(md_list)
    #post timesheet to model 
    # if req.method == 'POST':
    #     for item in wk_hrs_list:
    #         pending_timesheet = Timesheet( employee=userObj, day_worked_hours=item )
    #         pending_timesheet.save()
    #render PTO results
    return render(req, 'pto_summary.html')
    

# timesheet_date = models.DateField() 
#     day_worked_hours = models.DecimalField(max_digits=4, decimal_places=2)

# @login_required
# def timesheet_review(req):
#     user = req.user
#     print(user.id)
#     #headers
#     md_list = req.POST.getlist("month_day_list")
#     wkdy_list = req.POST.getlist("weekday_list")
#     #hours
#     wk_hrs = req.POST.getlist("hrs_worked")
#     pto_hrs = req.POST.getlist("hrs_pto")
#     wk_hrs = [float(hr) for hr in wk_hrs]
#     pto_hrs = [float(hr) for hr in pto_hrs]
#     tot_wk_hrs = sum(wk_hrs)
#     tot_pto_hrs = sum(pto_hrs)

#     return render(req, 'confirm_entry.html', 
#         {'wk_hrs': wk_hrs, 'pto_hrs': pto_hrs, 
#             'tot_wk_hrs': tot_wk_hrs, 'tot_pto_hrs': tot_pto_hrs,
#             'weekday_list': wkdy_list, 'month_day_list': md_list})
