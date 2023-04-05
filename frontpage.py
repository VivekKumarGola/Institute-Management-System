from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import ttk
import pymysql
from courseinsert import *
from coursefind import *
from courseupdate import *
from coursedelete import *
from feeplaninsert import *
from feeplanfind import *
from feeplanupdate import *
from feeplandelete import *
from enquiryinsert import *
from enquiryfind import *
from enquiryupdate import *
from enquirydelete import *
from adminregistration import *
from admindelete import *
from adminfind import *
from adminupdate import *
from batchdatainsert import *
from batchdatafind import *
from batchdataupdate import *
from batchdatadelete import *
from registrationinsert import *
from registrationfind import *
from registrationupdate import *
from registrationdelete import *
from batchshiftinsert import *
from batchshiftfind import *

t=tkinter.Tk()#make tkinter
t.geometry('1700x1700')#size set 

bg = PhotoImage(file='rrr.gif')
label1 = Label(t, image = bg)
label1.place(x = 0, y = 0)


l1=Label(t,text='Admin_Registration',bg='gray',fg='white',font=('arial',10),width=15,height=2)
l1.place(x=20,y=20)
bt1=Button(t,text='insert',bg='black',fg='white',width=10,font=10,command=admininsert)
bt1.place(x=20,y=70,height=40)
bt2=Button(t,text='find',bg='black',fg='white',width=10,font=10,command=adminfind)
bt2.place(x=20,y=110,height=40)
bt3=Button(t,text='update',bg='black',fg='white',width=10,font=10,command=adminupdate)
bt3.place(x=20,y=150,height=40)
bt4=Button(t,text='delete',bg='black',fg='white',width=10,font=10,command=admindelete)
bt4.place(x=20,y=190,height=40)

l2=Label(t,text='User_Registration',bg='gray',fg='white',font=('arial',10),width=15,height=2)
l2.place(x=170,y=20)
bt5=Button(t,text='insert',bg='black',fg='white',width=10,font=10)
bt5.place(x=170,y=70,height=40)
bt6=Button(t,text='find',bg='black',fg='white',width=10,font=10)
bt6.place(x=170,y=110,height=40)
bt7=Button(t,text='update',bg='black',fg='white',width=10,font=10)
bt7.place(x=170,y=150,height=40)
bt8=Button(t,text='delete',bg='black',fg='white',width=10,font=10)
bt8.place(x=170,y=190,height=40)

l4=Label(t,text='Enquiry_Details',bg='gray',fg='white',font=('arial',10),width=15,height=2)
l4.place(x=320,y=20)
bt13=Button(t,text='insert',bg='black',fg='white',width=10,font=10,command=enquiryinsert)
bt13.place(x=320,y=70,height=40)
bt14=Button(t,text='find',bg='black',fg='white',width=10,font=10,command=enquiryfind)
bt14.place(x=320,y=110,height=40)
bt15=Button(t,text='update',bg='black',fg='white',width=10,font=10,command=enquiryupdate)
bt15.place(x=320,y=150,height=40)
bt16=Button(t,text='delete',bg='black',fg='white',width=10,font=10,command=enquirydelete)
bt16.place(x=320,y=190,height=40)

l3=Label(t,text='Batch_Allocation',bg='gray',fg='white',font=('arial',10),width=15,height=2)
l3.place(x=20,y=280)
bt9=Button(t,text='insert',bg='black',fg='white',width=10,font=10,command=batchdatainsert)
bt9.place(x=20,y=330,height=40)
bt10=Button(t,text='find',bg='black',fg='white',width=10,font=10,command=batchdatafind)
bt10.place(x=20,y=370,height=40)
bt11=Button(t,text='update',bg='black',fg='white',width=10,font=10,command=batchdataupdate)
bt11.place(x=20,y=410,height=40)
bt12=Button(t,text='delete',bg='black',fg='white',width=10,font=10,command=batchdatadelete)
bt12.place(x=20,y=450,height=40)

l5=Label(t,text='Registration',bg='gray',fg='white',font=('arial',10),width=15,height=2)
l5.place(x=170,y=280)
bt17=Button(t,text='insert',bg='black',fg='white',width=10,font=10,command=registrationinsert)
bt17.place(x=170,y=330,height=40)
bt18=Button(t,text='find',bg='black',fg='white',width=10,font=10,command=registrationfind)
bt18.place(x=170,y=370,height=40)
bt19=Button(t,text='update',bg='black',fg='white',width=10,font=10,command=registrationupdate)
bt19.place(x=170,y=410,height=40)
bt20=Button(t,text='delete',bg='black',fg='white',width=10,font=10,command=registrationdelete)
bt20.place(x=170,y=450,height=40)

l6=Label(t,text='Batch_Shift',bg='gray',fg='white',font=('arial',10),width=15,height=2)
l6.place(x=320,y=280)
bt21=Button(t,text='insert',bg='black',fg='white',width=10,font=10,command=batchshiftinsert)
bt21.place(x=320,y=330,height=40)
bt22=Button(t,text='find',bg='black',fg='white',width=10,font=10,command=batchshiftfind)
bt22.place(x=320,y=370,height=40)
bt23=Button(t,text='update',bg='black',fg='white',width=10,font=10)
bt23.place(x=320,y=410,height=40)
bt24=Button(t,text='delete',bg='black',fg='white',width=10,font=10)
bt24.place(x=320,y=450,height=40)

l8=Label(t,text='Course_Details',bg='gray',fg='white',font=('arial',10),width=15,height=2)
l8.place(x=100,y=520)
bt29=Button(t,text='insert',bg='black',fg='white',width=10,font=10,command=courseinsert)
bt29.place(x=100,y=570,height=40)
bt30=Button(t,text='find',bg='black',fg='white',width=10,font=10,command=coursefind)
bt30.place(x=100,y=610,height=40)
bt31=Button(t,text='update',bg='black',fg='white',width=10,font=10,command=courseupdate)
bt31.place(x=100,y=650,height=40)
bt32=Button(t,text='delete',bg='black',fg='white',width=10,font=10,command=coursedelete)
bt32.place(x=100,y=690,height=40)

l9=Label(t,text='Fee_Plan',bg='gray',fg='white',font=('arial',10),width=15,height=2)
l9.place(x=250,y=520)
bt33=Button(t,text='insert',bg='black',fg='white',width=10,font=10,command=feeplaninsert)
bt33.place(x=250,y=570,height=40)
bt34=Button(t,text='find',bg='black',fg='white',width=10,font=10,command=feeplanfind)
bt34.place(x=250,y=610,height=40)
bt35=Button(t,text='update',bg='black',fg='white',width=10,font=10,command=feeplanupdate)
bt35.place(x=250,y=650,height=40)
bt36=Button(t,text='delete',bg='black',fg='white',width=10,font=10,command=feeplandelete)
bt36.place(x=250,y=690,height=40)
t.mainloop()