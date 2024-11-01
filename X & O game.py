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
x = randint(0,1)
if x == 1 :
    roud.set("x")
else :
    roud.set("o")

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

def rr() :
    y = randint(0, len(nb) - 1)
    if nb[y] == 1:
        global i1
        i1 = roud.get()
        but1.configure(text=roud.get())
        if roud.get() == "x":
            roud.set("o")
        else:
            roud.set("x")
        nb.remove(1)
        score()
    elif nb[y]  == 2:
        global i2
        i2 = roud.get()
        but2.configure(text=roud.get())
        if roud.get() == "x":
            roud.set("o")
        else:
            roud.set("x")
        nb.remove(2)
        score()
    elif nb[y] == 3:
        global i3
        i3 = roud.get()
        but3.configure(text=roud.get())
        if roud.get() == "x":
            roud.set("o")
        else:
            roud.set("x")
        nb.remove(3)
        score()
    elif nb[y] == 4:
        global i4
        i4 = roud.get()
        but4.configure(text=roud.get())
        if roud.get() == "x":
            roud.set("o")
        else:
            roud.set("x")
        nb.remove(4)
        score()
    elif nb[y] == 5:
        global i5
        i5 = roud.get()
        but5.configure(text=roud.get())
        if roud.get() == "x":
            roud.set("o")
        else:
            roud.set("x")
        nb.remove(5)
        score()
    elif nb[y] == 6:
        global i6
        i6 = roud.get()
        but6.configure(text=roud.get())
        if roud.get() == "x":
            roud.set("o")
        else:
            roud.set("x")
        nb.remove(6)
        score()
    elif nb[y] == 7:
        global i7
        i7 = roud.get()
        but7.configure(text=roud.get())
        if roud.get() == "x":
           roud.set("o")
        else:
            roud.set("x")
        nb.remove(7)
        score()
    elif nb[y] == 8:
        global i8
        i8 = roud.get()
        but8.configure(text=roud.get())
        if roud.get() == "x":
            roud.set("o")
        else:
            roud.set("x")
        nb.remove(8)
        score()
    elif nb[y] == 9:
        global i9
        i9 = roud.get()
        but9.configure(text=roud.get())
        if roud.get() == "x":
            roud.set("o")
        else:
            roud.set("x")
        nb.remove(9)
        score()
def robot() :
    if opt.get() == "العب بين شخصين" :
        pass
    elif opt.get() == "العب مع الحاسوب" :
        rr()

def b1() :
    global i1
    i1 = roud.get()
    but1.configure(text=roud.get())
    if roud.get() == "x" :
        roud.set("o")
    else :
        roud.set("x")
    nb.remove(1)
    score()
    robot()
def b2() :
    global i2
    i2 = roud.get()
    if roud.get() == "x" :
        but2.config(text="x")
        roud.set("o")
    else :
        but2.config(text="o")
        roud.set("x")
    nb.remove(2)
    score()
    robot()
def b3() :
    global i3
    i3 = roud.get()
    if roud.get() == "x" :
        but3.config(text="x")
        roud.set("o")
    else :
        but3.config(text="o")
        roud.set("x")
    nb.remove(3)
    score()
    robot()
def b4() :
    global i4
    i4 = roud.get()
    if roud.get() == "x" :
        but4.config(text="x")
        roud.set("o")
    else :
        but4.config(text="o")
        roud.set("x")
    nb.remove(4)
    score()
    robot()
def b5() :
    global i5
    i5 = roud.get()
    if roud.get() == "x" :
        but5.config(text="x")
        roud.set("o")
    else :
        but5.config(text="o")
        roud.set("x")
    nb.remove(5)
    score()
    robot()
def b6() :
    global i6
    i6 = roud.get()
    if roud.get() == "x" :
        but6.config(text="x")
        roud.set("o")
    else :
        but6.config(text="o")
        roud.set("x")
    nb.remove(6)
    score()
    robot()
def b7() :
    global i7
    i7 = roud.get()
    if roud.get() == "x" :
        but7.config(text="x")
        roud.set("o")
    else :
        but7.config(text="o")
        roud.set("x")
    nb.remove(7)
    score()
    robot()
def b8() :
    global i8
    i8 = roud.get()
    if roud.get() == "x" :
        but8.config(text="x")
        roud.set("o")
    else :
        but8.config(text="o")
        roud.set("x")
    nb.remove(8)
    score()
    robot()
def b9() :
    global i9
    i9 = roud.get()
    if roud.get() == "x" :
        but9.config(text="x")
        roud.set("o")
    else :
        but9.config(text="o")
        roud.set("x")
    nb.remove(9)
    score()
    robot()
def _clear() :
    ow.set(0)
    xw.set(0)
    n.set(0)

clear = Button(t,text="مسح",command=_clear)
clear.place(x=5,y=-2)

l1 = Label(t,text=": دور")\
    .place(x=90,y=-2)
l2 = Label(t,textvariable=roud)\
    .place(x=65,y=-2)
l3 = Label(t,text=": o")\
    .place(x=95,y=22)
l4 = Label(t,text=": x")\
    .place(x=95,y=45)
l5 = Label(t,text=": تعادل")\
    .place(x=25,y=31)
l6 = Label(t,textvariable=ow)\
    .place(x=75,y=22)
l7 = Label(t,textvariable=xw)\
    .place(x=75,y=45)
l8 = Label(t,textvariable=n)\
    .place(x=5,y=31)
opt.set("العب بين شخصين")
option = OptionMenu(t,opt,"العب بين شخصين","العب مع الحاسوب")
option.place(x=5,y=63)

but7 = Button(t,text="",command=b7,bg="white",height="1",width="4")
but7.place(x=0,y=95)
but8 = Button(t,text="",command=b8,bg="white",height="1",width="4")
but8.place(x=45,y=95)
but9 = Button(t,text="",command=b9,bg="white",height="1",width="4")
but9.place(x=90,y=95)
but4 = Button(t,text="",command=b4,bg="white",height="1",width="4")
but4.place(x=0,y=125)
but5 = Button(t,text="",command=b5,bg="white",height="1",width="4")
but5.place(x=45,y=125)
but6 = Button(t,text="",command=b6,bg="white",height="1",width="4")
but6.place(x=90,y=125)
but1 = Button(t,text="",command=b1,bg="white",height="1",width="4")
but1.place(x=0,y=155)
but2 = Button(t,text="",command=b2,bg="white",height="1",width="4")
but2.place(x=45,y=155)
but3 = Button(t,text="",command=b3,bg="white",height="1",width="4")
but3.place(x=90,y=155)

t.mainloop()