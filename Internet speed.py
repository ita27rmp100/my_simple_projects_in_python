from tkinter import *
from tkinter import messagebox
from speedtest import Speedtest
t = Tk()
t.title("Internet speed")
t.geometry("325x140")
t.config(bg="black")

download = Label(t,text="Download speed :",fg="yellow",font=("arial",16,"bold"),bg="black").place(x=5,y=5)
upload = Label(t,text="Upload speed :",fg="yellow",font=("arial",16,"bold"),bg="black").place(x=5,y=30)
ping = Label(t,text="Ping :",fg="yellow",font=("arial",16,"bold"),bg="black").place(x=5,y=55)

download_speed = Label(t,text="0 Mbps",fg="white",font=("arial",16,"bold"),bg="black")
download_speed.place(x=195,y=7)
upload_speed = Label(t,text="0 Mbps",fg="white",font=("arial",16,"bold"),bg="black")
upload_speed.place(x=172,y=32)
ping_ = Label(t,text="0 Ms",fg="white",font=("arial",16,"bold"),bg="black")
ping_.place(x=75,y=57)

def speed() :
    try :
        l = Speedtest()
        download_speed.config(text=str(f"{l.download()/1048576:03.2f} Mbps"))
        upload_speed.config(text=str(f"{l.upload()/1048576:03.2f} Mbps"))
        ping_.config(text=str(f"{l.results.ping:03.2f} Ms"))
        messagebox.showinfo("Internet speed","Internet speed was calculated")
    except :
        messagebox.showerror("Internet speed","there is  no Internet")


start = Button(t,text="start",bg="yellow",fg="gold",bd=0,command=speed,font=("arial",16)).place(x=140,y=90)

t.mainloop()
