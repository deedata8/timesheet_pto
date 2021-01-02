from datetime import datetime, timedelta
import datetime as dt

#get current week's timesheet dates 
def get_week(m_d_y_str):
    #convert to datetime obj
    date_ = datetime.strptime(m_d_y_str, '%m/%d/%Y') 
    #obtain Monday of that week
    monday = date_ - timedelta(days=date_.weekday())
        
    #add 7 days from date
    md_list = []
    wkdy_list = []
    for i in range(7):
        date = monday + timedelta(days=i)
        md = date.strftime('%b-%d')
        md_list.append(md)
        #print(md_list)
        weekday = date.strftime("%A")
        wkdy_list.append(weekday)
        #print(wkdy_list)
    
    return wkdy_list, md_list