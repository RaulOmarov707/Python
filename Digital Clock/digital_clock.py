                            # DIGITAL CLOCK PROJECT with Tkinter Module in Python

from tkinter import *
from datetime import datetime

# TCL=TOOL COMMAND LANGUAGE,TK-TOOL KIT
# asterisk
# colors
color1="#3d3d3d"
color2="#21c25c"



root=Tk()
root.title("Digital Clock")
root.geometry('480x200')
root.resizable(width=False,height=False)
root.configure(background=color1)



l1=Label(root, font=('Arial 80'), bg=color1, fg=color2)
l1.grid(row=0, column=0, sticky=NW)



l2=Label(root, font=('Arial 30'), bg=color1, fg=color2)
l2.grid(row=1, column=0, sticky=NW)



def clock():
        time=datetime.now()
        hour=time.strftime("%H:%M:%S")
        weekday=time.strftime("%A")
        day=time.day
        month=time.strftime("%b") 
        year=time.strftime("%Y")
        l1.config(text=hour)
        l1.after(200,clock)
        l2.config(text=weekday+ " " + str(day) + "/" + str(month) + "/" + (year))



clock()
# FPS-FRAMES PER SECOND
root.mainloop()