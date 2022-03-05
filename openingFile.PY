# import urllib.request
import urllib2  
from datetime import date, timedelta


url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/"
# file = urllib.request.urlopen(url)

for x in range(7):
    theDate = date.today() - timedelta(days=7)
    currentUrl = url + theDate.strftime("%m-%d-%Y")
    currentUrl = currentUrl + ".csv"
    # file = urllib.request.urlopen(url)
    print(currentUrl)
    content=urllib2.urlopen(currentUrl)

# for line in file:
for line in content:  
    print (line) 
