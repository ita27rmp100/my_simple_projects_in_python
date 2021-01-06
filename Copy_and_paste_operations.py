from tkinter import *
import pyautogui
t = Tk()

def copy() :
    pyautogui.hotkey("ctrl", "c")
def cut() :
    pyautogui.hotkey("ctrl", "v")
def paste() :
    pyautogui.hotkey("ctrl", "x")

my_menu = Menu(t)
file_menu = Menu(my_menu)
my_menu.add_command(label="copy",command=lambda :pyautogui.hotkey("ctrl","c"))
my_menu.add_command(label="cut",command=lambda :pyautogui.hotkey("ctrl","x"))
my_menu.add_command(label="paste",command=lambda :pyautogui.hotkey("ctrl","v"))

def my_pop(e) :
    my_menu.tk_popup(e.x_root,e.y_root)

t.bind("<Button-3>",my_pop)

t.mainloop()
