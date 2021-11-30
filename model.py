import tkinter as tk
import time

class Timer(object):
    def __init__(self, master, **kwargs):
        self._active = False
        self._sec = 0
        self._min = 0

        self.master=master
        pad=3
        self._geom='800x400+0+0'
        master.config(background="black")
        master.title("Countdown")
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)

        self.time = tk.StringVar()
        self.time_label = tk.Label(self.master,
                                   textvariable=self.time,
                                   fg="#FFFFFF",
                                   font=("Arial", 200, "bold"),
                                   width=master.winfo_screenwidth()-pad,
                                   pady=4,
                                   bd=4,
                                   bg="#000",
                                   anchor=tk.CENTER,
                                   justify='center')
        self.time_label.grid(column=0, row=0)
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        print(f"setting active to {value}")
        self._active = value

    @property
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self,value):
        print(f'setting sec to {value}')
        self._sec = value

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        print(f'setting minutes to {value}')
        self._min = value

    def start_countdown(self):
        if self.sec < 10:
            sec_spacer = '0'
        else:
            sec_spacer = ''

        if self.min < 10:
            min_spacer = '0'
        else:
            min_spacer = ''


        self.secondss = self.time.set(f'{min_spacer}{self.min}:{sec_spacer}{self.sec}')
        self.time_label.config(text="Countdown", fg="#FFFFFF")

        if self._active:

            if self.sec > 0:
                self.sec -= 1
                self.master.after(1000, self.start_countdown)


            elif self.sec == 0 and self.min > 0:
                self.min -= 1
                self.sec = 59
                self.master.after(1000, self.start_countdown)

            elif self.sec == 0 and self.min == 0:
                self.time_label.config(text="Countdown End", fg="#FF0000")
        else:
            print(f'Time: {self.min}:{self.sec}')

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom=geom

#root=tk.Tk()
#app=Timer(root)
#app.start_countdown(1,1)
#root.mainloop()


