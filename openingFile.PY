import urllib2  
from datetime import date, timedelta


url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/"

for x in range(7):
    theDate = date.today() - timedelta(days=7)
    currentUrl = url + theDate.strftime("%m-%d-%Y")
    currentUrl = currentUrl + ".csv"
    content=urllib2.urlopen(currentUrl)
    for line in content: 
