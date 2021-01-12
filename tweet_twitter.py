from tkinter import *
from tkinter import messagebox
import pyautogui , webbrowser , time , speedtest
t = Tk()
t.title("tweet twitter")
t.geometry("405x440")
t.resizable(0,0)

text_tweet = Text(t,width=50,height=25)
text_tweet.place(x=0,y=0)

link_tweet = Entry(t,width=30)
link_tweet.place(x=200,y=412)
link_tweet.insert(0,"أدخل رابط التغريدة التي تريد الرد عليها")

def tweet_simple() :
    st = speedtest.Speedtest().download()
    try :
        webbrowser.open("https://twitter.com/home")
        time.sleep(10)
        for i in range(14):
            pyautogui.hotkey("Tab")
        pyautogui.hotkey("enter")
        time.sleep(20)
        pyautogui.write(text_tweet.get("1.0","end"))
        for i in range(8):
            pyautogui.hotkey("Tab")
        pyautogui.hotkey("enter")
    except :
        messagebox.showerror("خطأ","لا توجد انترنت")
def reply() :
    st = speedtest.Speedtest().download()
    try :
        webbrowser.open(link_tweet.get())
        time.sleep(20)
        for i in range(24):
            pyautogui.hotkey("Tab")
        pyautogui.hotkey("enter")
        time.sleep(3)
        pyautogui.write(text_tweet.get("1.0", "end"))
        for i in range(6):
            pyautogui.hotkey("Tab")
        pyautogui.hotkey("enter")
    except :
        messagebox.showerror("خطأ","لا توجد انترنت")
def thread() :
    st = speedtest.Speedtest().download()
    try :
        webbrowser.open(link_tweet.get())
        time.sleep(20)
        for i in range(25):
            pyautogui.hotkey("Tab")
        pyautogui.hotkey("enter")
        time.sleep(3)
        pyautogui.write(text_tweet.get("1.0", "end"))
        for i in range(7):
            pyautogui.hotkey("Tab")
        pyautogui.hotkey("enter")
    except :
        messagebox.showerror("خطأ","لا توجد انترنت")

tweet = Button(t,text="tweet",bg="lightblue",fg="white",command=tweet_simple) #دال لنشر تغريدات
tweet.place(x=5,y=410)

reply = Button(t,text="reply",fg="white",bg="lightblue",command=reply) # دالة للرد على التغريدات و ليس الردود
reply.place(x=50,y=410)

reply = Button(t,text="reply/thread",fg="white",bg="lightblue",command=thread) # دالة للرد على تغريداتي
reply.place(x=95,y=410)

t.mainloop()
