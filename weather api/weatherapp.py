from pprint import *
import tkinter
import requests
from tkinter import *
import datetime
from datetime import date

root = Tk()
root.geometry("900x700")
root.title("The Weather App- by surya")
img = PhotoImage(file='sun_behind_cloud-512.png')
root.tk.call('wm', 'iconphoto', root._w, img)
# root.resizable(False, False)


C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file="Cloud-Background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.grid()


def show():
    x = entry_city.get()
    y = enter_lat.get()
    z = enter_lon.get()
    print(x)
    print(y)
    print(z)


    if x != "":

        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=c3496ec82796d53908eb44fff87eac32&units=metric".format(
            x)
        res = requests.get(url)
        data = res.json()
    else:

        res = requests.get('https://ipinfo.io/')
        data = res.json()
        # location = data['loc'].split(',')
        # latitude = location[0]
        # longitude = location[1]
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=d1a7ed688e1b9155f95106d9a55b9ab0&units=metric'.format(
            y, z)

        res = requests.get(url)
        data = res.json()

    temp = str(data['main']['temp']) + '  degree celcius'
    pressure = str(data['main']['pressure']) + ' hPa'
    humidity = str(data['main']['humidity']) + '%'
    wind_speed = str(data['wind']['speed']) + 'm/s'
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    name = data ['name']
    description = data['weather'][0]['description']
    country = data['sys']['country']

    print('Temperature : {} degree calcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('description : {}'.format(description))
    print('pressure : {}'.format(pressure))
    print('humidity : {}'.format(humidity))
    print('Country:{}'.format(country))
    current_date = datetime.date.today()
    print(current_date)


    date.config(text=current_date,font='bold 20')
    mi.config(text=temp)
    mi1.config(text=wind_speed)
    mi2.config(text=latitude)
    mi3.config(text=longitude)
    mi4.config(text=description)
    mi5.config(text=pressure)
    mi6.config(text=humidity)
    mi7.config(text=name)
    #ci.config(text=entry_city.get())

date=Label(root,text="",font=30,bg='#%02x%02x%02x' % (64, 204, 208))
date.grid(row=3,column=1,pady=4)
label_city = Label(root, text="Search Weather of your City Here : - ", width=30, font=90)
label_city.grid(row=0, columnspan=2, pady=6)
label_city = Label(root, text="Search Weather For Latitude and Longitude : - ", width=40, font=90)
label_city.grid(row=1, columnspan=2, pady=6)
entry_city = Entry(root, width=30)
entry_city.grid(row=0, column=3)
enter_lat = Entry(root, width=30)
enter_lat.grid(row=1, column=3)
enter_lon = Entry(root, width=30)
enter_lon.grid(row=1, column=4,padx=4)
b = Button(root, text="Show Me!!", width=15, bg='grey', fg='black', command=show)
b.grid(row=2, column=3)

# ci = Label(root, text="You Search For :- ")
# ci.grid(row=3, column=0)

li = Label(root, text="  The Temperature of Required City is : - ", font='bold 15')
li.grid(row=4, sticky=E)
l2 = Label(root, text="The Wind Speed Of Required City is : - ", font='bold 15')
l2.grid(row=5, sticky=E)
l3 = Label(root, text="The Lattitude Of Required City is : - ", font='bold 15')
l3.grid(row=6, sticky=E)
l4 = Label(root, text=" The Longitude Of Required City is : - ", font='bold 15')
l4.grid(row=7, sticky=E)
l5 = Label(root, text="  The Description Of Required City is : - ", font='bold 15')
l5.grid(row=8, sticky=E)
l6 = Label(root, text="  The Pressure Of Required City is : - ", font='bold 15')
l6.grid(row=9, sticky=E)
l7 = Label(root, text="  The humidity Of Required City is : - ", font='bold 15')
l7.grid(row=10, sticky=E)
l8 = Label(root, text="  The Area you Searched is : - ", font='bold 15')
l8.grid(row=11, sticky=E)

# ci = Label(root, text=" -- ", font='bold 20')
# ci.grid(row=3, column=1)
mi = Label(root, text=" -- ")
mi.grid(row=4, column=1)
mi1 = Label(root, text=" -- ")
mi1.grid(row=5, column=1)
mi2 = Label(root, text=" -- ")
mi2.grid(row=6, column=1)
mi3 = Label(root, text=" -- ")
mi3.grid(row=7, column=1)
mi4 = Label(root, text=" -- ")
mi4.grid(row=8, column=1)
mi5 = Label(root, text=" -- ")
mi5.grid(row=9, column=1)
mi6 = Label(root, text=" -- ")
mi6.grid(row=10, column=1)
mi7 = Label(root, text=" -- ", font='bold 20')
mi7.grid(row=11, column=1)
country=Label(root,text="",font=15)
country.grid(row=13,column=0)
root.mainloop()
