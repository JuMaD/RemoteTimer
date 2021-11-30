import time
from pizco import Proxy
from tkinter import *

proxy = Proxy('tcp://127.0.0.1:8000')

#todo: Implement method that gets timings & Names out of a csv file and accesses next talk via "next talk" button

def send_time():
    print("Sending time ...")
    proxy.active = False
    proxy.sec = int(seconds.get())
    proxy.min = int(minutes.get())
    proxy.start_countdown()



def pause_continue():
    if proxy.active == False:
        proxy.active = True
        pc_btn_text.set("Pause")
        proxy.start_countdown()

    elif proxy.active == True:
        proxy.active = False
        pc_btn_text.set("Continue")

def reset():
    #proxy.active = False
    send_time()

def start_time():
    proxy.active = True
    proxy.start_countdown()

def add_time(amin=0, asec=10):
    proxy.active = False
    proxy.min += int(addminutes.get())
    proxy.sec += int(addseconds.get())
    proxy.start_countdown()
    proxy.active = True







master = Tk()
master.title("Countdown Control")
Label(master, text="Time").grid(row=0)
Label(master, text="min").grid(row=0, column=2)
Label(master, text="sec").grid(row=0, column=4)

SecondsVar = IntVar()
SecondsVar = proxy.sec
Label(master, text=SecondsVar).grid(row=0, column=5)

minutes = Entry(master)
minutes.insert(2,'0')
minutes.grid(row=0, column=1)

seconds = Entry(master)
seconds.insert(2,'0')
seconds.grid(row=0, column=3)

addminutes = Entry(master)
addminutes.insert(2,'0')
addminutes.grid(row=4, column=1)

addseconds = Entry(master)
addseconds.insert(2,'0')
addseconds.grid(row=4, column=3)

pc_btn_text = StringVar()
pc_btn_text.set('Pause')
Button(master, text='Start', command=start_time).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Send Time', command=send_time).grid(row=3, column=1, sticky=W, pady=4)
Button(master, textvariable=pc_btn_text, command=pause_continue).grid(row=3, column=2, sticky=W, pady=4)
Button(master, text="Reset", command=reset).grid(row=3, column=3, sticky=W, pady=4)

Button(master, text="add time", command=add_time).grid(row=5, column=3, sticky=W, pady=4)


mainloop()





