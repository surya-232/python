import request 

city=input("enter city name")

url=""

res=request.get(url)

data=res.json()

temp=data['main']['temp']
wind_speed=data['wind']['speed']

latitude=data['coard']['lat']
longitude=data['coard']['lon']

description=data['weather'][0]['description']

print('Temprature : {} degree calcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Lantitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('description : {}'.format(description))