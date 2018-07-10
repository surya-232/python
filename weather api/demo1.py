from pprint import *
import tkinter
import requests
from tkinter import *
root=Tk()
root.geometry("300x500")
root.title("Sunshine")
#img = PhotoImage(file='weather.png')
#root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(False,False)
def show():
    x=entry_city.get()
    print(x)
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=c3496ec82796d53908eb44fff87eac32&unit=metrics".format(x)
    res = requests.get(url)
    data = res.json()
    #pprint(data)
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    description = data['weather'][0]['description']

    print('Temprature : {} degree calcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Lantitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('description : {}'.format(description))



label_city=Label(root,text="City",width=10,font=90)
label_city.grid(row=0,columnspan=2,pady=6)
entry_city=Entry(root,width=30)
entry_city.grid(row=0,column=3)
b=Button(root,text="Show Weather",width=15,bg='red',fg='black',command=show)
b.grid(row=1,column=3)




root.mainloop()