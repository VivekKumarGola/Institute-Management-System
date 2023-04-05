import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from adminlogin import*
from userlogin import*
t=tkinter.Tk()#make tkinter
import pymysql

t.geometry('1900x1900')
c=Canvas(width=650,height=1000)
c.place(x=0,y=0)
bg4= PhotoImage(file='login.gif')
label4 = Label(c, image = bg4)
label4.place(x = 0, y = 0)
bg5 = PhotoImage(file='user.gif')
label5 = Label(c, image = bg5,width=200,height=200)
label5.place(x = 100, y = 250)
bg6 = PhotoImage(file='user.gif')
label6 = Label(c, image = bg6,width=200,height=200)
label6.place(x = 400, y = 250)
b1=Button(c,text="Admin",bg='gray',fg='white',font=('arial',14),width=18,height=2,command=Alogin)
b1.place(x=100,y=460)
b2=Button(c,text="User",bg='gray',fg='white',font=('arial',14),width=18,height=2,command=userlogin)
b2.place(x=400,y=460)
t.mainloop()

