import tkinter
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x500")
root.title("Sunshine")
#img = PhotoImage(file='weather.png')
#root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(False,False)
def show():
    print(entry_city.get())
label_city=Label(root,text="City",width=10,font=90)
label_city.grid(row=0,columnspan=2,pady=6)
entry_city=Entry(root,width=30)
entry_city.grid(row=0,column=3)
b=Button(root,text="Show Weather",width=15,bg='red',fg='black',command=show)
b.grid(row=1,column=3)

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "sun_behind_cloud-512.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.grid()
root.mainloop()