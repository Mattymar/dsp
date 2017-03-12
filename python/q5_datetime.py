# Hint:  use Google to find python function
from datetime import datetime

def days_elapsed(start, stop, format):
    '''
    Returns number of days between two dates.
    Must provide start and stop dates and their format.
    '''
    a = datetime.strptime(start, format)
    b = datetime.strptime(stop, format)
    return (b - a).days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
print(days_elapsed(date_start, date_stop, "%m-%d-%Y"))

####b)  
date_start = '12312013'  
date_stop = '05282015'  
print(days_elapsed(date_start, date_stop, "%m%d%Y"))

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
print(days_elapsed(date_start, date_stop, "%d-%b-%Y"))
