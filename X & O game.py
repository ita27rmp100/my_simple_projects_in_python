from tkinter import *
from tkinter import messagebox
from random import randint

t = Tk()
t.title("tic_tac_toe")
t.geometry("130x185")
t.resizable(0,0)
roud = StringVar()
xw = IntVar()
ow = IntVar()
n= IntVar()
opt = StringVar()
roud.set(['x','o'][randint(0,1)])
nb = list(range(1,10))
def caa() :
    nb.clear()
    for i in range(1,11) :
        nb.append(i)

def winner_x() :
    xw.set(xw.get() + 1)
    messagebox.showinfo("الفائز هو x", "تحصل اللاعب إكس على نقطة")
    caa()
    but1.config(text="");but2.config(text="");but3.config(text="");but4.config(text="");but5.config(text="");but6.config(text="");but7.config(text="");but8.config(text="");but9.config(text="")
def winner_o() :
    ow.set(xw.get() + 1)
    messagebox.showinfo("الفائز هو o", "تحصل اللاعب أو على نقطة")
    caa()
    but1.config(text="");but2.config(text="");but3.config(text="");but4.config(text="");but5.config(text="");but6.config(text="");but7.config(text="");but8.config(text="");but9.config(text="")

def score() :
    if but1["text"] == but2["text"] == but3["text"] == "x":
        winner_x()
    elif but1["text"] == but2["text"] == but3["text"] == "o":
        winner_o()
    elif but4["text"] == but5["text"] == but6["text"] == "x":
        winner_x()
    elif but4["text"] == but5["text"] == but6["text"] == "o":
        winner_o()
    elif but7["text"] == but8["text"] == but9["text"] == "x":
        winner_x()
    elif but7["text"] == but8["text"] == but9["text"] == "o":
        winner_o()
    elif but1["text"] == but4["text"] == but7["text"] == "x":
        winner_x()
    elif but1["text"] == but4["text"] == but7["text"] == "o":
        winner_o()
    elif but2["text"] == but5["text"] == but8["text"] == "x":
        winner_x()
    elif but2["text"] == but5["text"] == but8["text"] == "o":
        winner_o()
    elif but3["text"] == but6["text"] == but9["text"] == "x":
        winner_x()
    elif but3["text"] == but6["text"] == but9["text"] == "o":
        winner_o()
    elif but1["text"] == but5["text"] == but9["text"] == "x":
        winner_x()
    elif but1["text"] == but5["text"] == but9["text"] == "o":
        winner_o()
    elif but3["text"] == but5["text"] == but7["text"] == "x":
        winner_x()
    elif but3["text"] == but5["text"] == but7["text"] == "o":
        winner_o()
    else :
        j = [but1["text"],but2["text"],but3["text"],but4["text"],but5["text"],but6["text"],but7["text"],but8["text"],but9["text"]]
        if j.count("") == 0 :
            messagebox.showinfo("", "تعادل")
            caa()
            n.set(n.get()+1);but1.config(text="");but2.config(text="");but3.config(text="");but4.config(text="");but5.config(text="");but6.config(text="");but7.config(text="");but8.config(text="");but9.config(text="")
    roud.set('o') if roud.get() == 'x' else roud.set('x')

def rr() :
    y = randint(0, len(nb) - 1)
    if nb[y] == 1:
        but1.configure(text=roud.get())
    elif nb[y]  == 2:
        but2.configure(text=roud.get())
    elif nb[y] == 3:
        but3.configure(text=roud.get())
    elif nb[y] == 4:
        but4.configure(text=roud.get())
    elif nb[y] == 5:
        but5.configure(text=roud.get())
    elif nb[y] == 6:
        but6.configure(text=roud.get())
    elif nb[y] == 7:
        but7.configure(text=roud.get())
    elif nb[y] == 8:
        but8.configure(text=roud.get())
    elif nb[y] == 9:
        but9.configure(text=roud.get())
    nb.remove(nb[y])
    score()

def robot() :
    if opt.get() == "العب بين شخصين" :
        pass
    elif opt.get() == "العب مع الحاسوب" :
        rr()

def b1() :
    but1.configure(text=roud.get())
    nb.remove(1)
    score()
    robot()
def b2() :
    but2.configure(text=roud.get())
    nb.remove(2)
    score()
    robot()
def b3() :
    but3.configure(text=roud.get())
    nb.remove(3)
    score()
    robot()
def b4() :
    but4.configure(text=roud.get())
    nb.remove(4)
    score()
    robot()
def b5() :
    but5.config(text=roud.get())
    nb.remove(5)
    score()
    robot()
def b6() :
    but6.configure(text=roud.get())
    nb.remove(6)
    score()
    robot()
def b7() :
    but7.configure(text=roud.get())
    nb.remove(7)
    score()
    robot()
def b8() :
    but8.configure(text=roud.get())
    nb.remove(8)
    score()
    robot()
def b9() :
    but9.configure(text=roud.get())
    nb.remove(9)
    score()
    robot()
def _clear() :
    ow.set(0)
    xw.set(0)
    n.set(0)

# GUI of game
clear = Button(t,text="مسح",command=_clear)
clear.place(x=5,y=-2)

l1 = Label(t,text=": دور").place(x=90,y=-2)
l2 = Label(t,textvariable=roud).place(x=65,y=-2)
l3 = Label(t,text=": o").place(x=95,y=22)
l4 = Label(t,text=": x").place(x=95,y=45)
l5 = Label(t,text=": تعادل").place(x=25,y=31)
l6 = Label(t,textvariable=ow).place(x=75,y=22)
l7 = Label(t,textvariable=xw).place(x=75,y=45)
l8 = Label(t,textvariable=n).place(x=5,y=31)
opt.set("العب بين شخصين")
option = OptionMenu(t,opt,"العب بين شخصين","العب مع الحاسوب").place(x=5,y=63)

but7 = Button(t,text="",command=b7,bg="white",height="1",width="4").place(x=0,y=95)
but8 = Button(t,text="",command=b8,bg="white",height="1",width="4").place(x=45,y=95)
but9 = Button(t,text="",command=b9,bg="white",height="1",width="4").place(x=90,y=95)
but4 = Button(t,text="",command=b4,bg="white",height="1",width="4").place(x=0,y=125)
but5 = Button(t,text="",command=b5,bg="white",height="1",width="4").place(x=45,y=125)
but6 = Button(t,text="",command=b6,bg="white",height="1",width="4").place(x=90,y=125)
but1 = Button(t,text="",command=b1,bg="white",height="1",width="4").place(x=0,y=155)
but2 = Button(t,text="",command=b2,bg="white",height="1",width="4").place(x=45,y=155)
but3 = Button(t,text="",command=b3,bg="white",height="1",width="4").place(x=90,y=155)

t.mainloop()
