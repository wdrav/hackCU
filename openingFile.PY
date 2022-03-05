<<<<<<< HEAD
# import urllib.request
from operator import contains
=======
>>>>>>> e2c3826628e260a619255607d805ea409ae799f1
import urllib2  
from datetime import date, timedelta


url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/"

for x in range(7):
    theDate = date.today() - timedelta(days=7)
    currentUrl = url + theDate.strftime("%m-%d-%Y")
    currentUrl = currentUrl + ".csv"
    content=urllib2.urlopen(currentUrl)
<<<<<<< HEAD

# for line in file:
substring = "Colorado"
for line in content:  
    if substring in line:
        print (line) 
=======
    for line in content: 
>>>>>>> e2c3826628e260a619255607d805ea409ae799f1
