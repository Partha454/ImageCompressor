from tkinter import *
import tkinter as tk
import PIL.Image
import PIL.ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("650x500+300+200")
root.resizable(False,False)

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=35e20c964e7a115f70dd8b9d00f3baff"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
                                        
    
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)



    

Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=120,y=120)

Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

name=Label(root,font=("arial",10,"bold"))
name.place(x=20,y=100)
clock=Label(root,font=("Helvetica",10))
clock.place(x=30,y=130)

label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=20,y=400)
label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=90,y=400)
label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=205,y=400)
label3=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=360,y=400)

t=Label(font=("arial",30,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",10,"bold"))
c.place(x=400,y=250)
w=Label(text="...",font=("arial",30,"bold"),bg="#1ab5ef")
w.place(x=30,y=425)
h=Label(text="...",font=("arial",30,"bold"),bg="#1ab5ef")
h.place(x=120,y=425)
d=Label(text="...",font=("arial",30,"bold"),bg="#1ab5ef")
d.place(x=200,y=425)
p=Label(text="...",font=("arial",30,"bold"),bg="#1ab5ef")
p.place(x=400,y=425)



root.mainloop()






