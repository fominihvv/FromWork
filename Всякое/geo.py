from geopy.geocoders import Nominatim
import requests




"""geolocator = Nominatim(user_agent="UserAgent: Mozilla/5.0 (Windows NT 10")
location = geolocator.geocode("Saint Petersburg City, Russia").raw
coordinates = location['lat'], location['lon']
#('59.938732', '30.316229')
location = geolocator.reverse(coordinates)
print(location)"""

s_city = "Saint Petersburg, RU"
city_id = 0
appid = '838bdf33f727790b08f4ffeec808d51a'

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    print(data)
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass