

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
t=tkinter.Tk()#make tkinter
t.geometry('1700x1700')
#from datetime import datetime
import datetime
d=datetime.datetime.now()
#print(d)
e=(d.day,d.month,d.year,d.hour,d.minute,d.minute,d.second)

    
e2=Entry(t,width=40)
e2.place(x=420,y=350,height=30)
e2.insert(0,e)



    
t.mainloop()




