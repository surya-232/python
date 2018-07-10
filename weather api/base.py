import requests
from pprint import  *

city=input("enter city name")

url= "https://api.openweathermap.org/data/2.5/weather?q={}&appid=c3496ec82796d53908eb44fff87eac32&unit=metrics".format(city)

res=requests.get(url)

data=res.json()
pprint(data)
temp=data['main']['temp']
wind_speed=data['wind']['speed']

latitude=data['coord']['lat']
longitude=data['coord']['lon']

description=data['weather'][0]['description']

print('Temprature : {} degree calcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Lantitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('description : {}'.format(description))