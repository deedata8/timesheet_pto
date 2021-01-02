from django.shortcuts import render
from .calcs import get_week

def index(req):
    return render(req, 'index_timesheet.html')

def entry(req):
    return render(req, 'set_date.html')


def get_timesheet(req):
    input = str(req.GET["date"])
    if input != '':
        #get current week's timesheet header dates and days
        wkdy_list, md_list = get_week(input)
    else:
        return render(req, 'set_date.html')

    return render(req, 'set_date.html', 
        {'weekday_list': wkdy_list, 'month_day_list': md_list})


def timesheet_review(req):
    #headers
    md_list = req.POST.getlist("month_day_list")
    wkdy_list = req.POST.getlist("weekday_list")
    #hours
    wk_hrs = req.POST.getlist("hrs_worked")
    pto_hrs = req.POST.getlist("hrs_pto")
    wk_hrs = [float(hr) for hr in wk_hrs]
    pto_hrs = [float(hr) for hr in pto_hrs]
    tot_wk_hrs = sum(wk_hrs)
    tot_pto_hrs = sum(pto_hrs)

    return render(req, 'confirm_entry.html', 
        {'wk_hrs': wk_hrs, 'pto_hrs': pto_hrs, 
            'tot_wk_hrs': tot_wk_hrs, 'tot_pto_hrs': tot_pto_hrs,
            'weekday_list': wkdy_list, 'month_day_list': md_list})


def pto_summary(req):
    return render(req, 'pto_summary.html')
    


