import requests  # requesting url's
import json
import geocoder
from dateutil import tz
from datetime import datetime
def tc(t):
    t = int(t)
    utc = datetime.fromtimestamp(t)
    itc_time = utc.astimezone(tz.gettz('ITC'))
    return itc_time


# converts kelvin to celcius
def tempConverter(temp):
    temp = int(temp)
    temp = temp-273.15
    return temp


# function to tell weather
def weather():
    g = geocoder.ip('me')
    lat = g.latlng[0]
    lon = g.latlng[1]
    api_key = "***********************"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    url = base_url + "lat="+str(lat)+"&lon="+str(lon) + \
        "&exclude=hourly,daily&appid=" + api_key
    response = requests.get(url)
    response.raise_for_status()
    w = json.loads(response.text)
    print('date = '+str(tc(w['current']['dt'])))
    print("sunrise = "+str(tc(w['current']['sunrise'])))
    print("sunset = "+str(tc(w['current']['sunset'])))
    print("Temperature = "+str(round(tempConverter(w['current']['temp']), 2))+" C")
    print("feels like = " +
          str(round(tempConverter(w['current']['feels_like']), 2))+" C")
