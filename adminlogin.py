import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from courseinsert import *
from coursefind import *
from courseupdate import *
from coursedelete import *
from userinsert import *
from userfind import *
from userupdate import *
from userdelete import *
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

def Alogin():
    
    def filldatatwo():
         db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
         cur=db.cursor()
         x=[]
         s="select admin_id from admin "
         cur.execute(s)
         data=cur.fetchall()
         for res in data:
             x.append(res[0])
         return(x)
    
   
    def pas():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=e1.get()
        ps=e2.get()
        
        s="select password from admin where admin_id='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        #ps=StringVar()
        #y=e2.get()
        if ps=="" and x=="":
            messagebox.showinfo("error","fill id or password..")
        elif ps=="":
            messagebox.showinfo("error","fill required password..")
        elif x=="":
            messagebox.showinfo("error","fill required id..")
        elif ps==data[0]:
            messagebox.showinfo("error","Login Successful..")
            c=Canvas(width=1900,height=1900)
            c.place(x=0,y=0)
            #t=tkinter.Tk()#make tkinter
            #t.geometry('1900x1900')
            
            bg = PhotoImage(file='rrr.gif')
            label1 = Label(c, image = bg)
            label1.place(x = 0, y = 0)
            
            
            l1=Label(c,text='Admin_Registration',bg='gray',fg='white',font=('arial',10),width=15,height=2)
            l1.place(x=20,y=20)
            bt1=Button(c,text='insert',bg='black',fg='white',width=10,font=10,command=admininsert)
            bt1.place(x=20,y=70,height=40)
            
            bt2=Button(c,text='find',bg='black',fg='white',width=10,font=10,command=adminfind)
            bt2.place(x=20,y=110,height=40)
            bt3=Button(c,text='update',bg='black',fg='white',width=10,font=10,command=adminupdate)
            bt3.place(x=20,y=150,height=40)
            bt4=Button(c,text='delete',bg='black',fg='white',width=10,font=10,command=admindelete)
            bt4.place(x=20,y=190,height=40)
            
            l2=Label(c,text='User_Registration',bg='gray',fg='white',font=('arial',10),width=15,height=2)
            l2.place(x=170,y=20)
            bt5=Button(c,text='insert',bg='black',fg='white',width=10,font=10,command=userinsert)
            bt5.place(x=170,y=70,height=40)
            bt6=Button(c,text='find',bg='black',fg='white',width=10,font=10,command=userfind)
            bt6.place(x=170,y=110,height=40)
            bt7=Button(c,text='update',bg='black',fg='white',width=10,font=10,command=userupdate)
            bt7.place(x=170,y=150,height=40)
            bt8=Button(c,text='delete',bg='black',fg='white',width=10,font=10,command=userdelete)
            bt8.place(x=170,y=190,height=40)
            
            l4=Label(c,text='Enquiry_Details',bg='gray',fg='white',font=('arial',10),width=15,height=2)
            l4.place(x=320,y=20)
            bt13=Button(c,text='insert',bg='black',fg='white',width=10,font=10,command=enquiryinsert)
            bt13.place(x=320,y=70,height=40)
            bt14=Button(c,text='find',bg='black',fg='white',width=10,font=10,command=enquiryfind)
            bt14.place(x=320,y=110,height=40)
            bt15=Button(c,text='update',bg='black',fg='white',width=10,font=10,command=enquiryupdate)
            bt15.place(x=320,y=150,height=40)
            bt16=Button(c,text='delete',bg='black',fg='white',width=10,font=10,command=enquirydelete)
            bt16.place(x=320,y=190,height=40)
            
            l3=Label(c,text='Registration',bg='gray',fg='white',font=('arial',10),width=15,height=2)
            l3.place(x=20,y=280)
            bt9=Button(c,text='insert',bg='black',fg='white',width=10,font=10,command=registrationinsert)
            bt9.place(x=20,y=330,height=40)
            bt10=Button(c,text='find',bg='black',fg='white',width=10,font=10,command=registrationfind)
            bt10.place(x=20,y=370,height=40)
            bt11=Button(c,text='update',bg='black',fg='white',width=10,font=10,command=registrationupdate)
            bt11.place(x=20,y=410,height=40)
            bt12=Button(c,text='delete',bg='black',fg='white',width=10,font=10,command=registrationdelete)
            bt12.place(x=20,y=450,height=40)
            
            l5=Label(c,text='Batch_Allocation',bg='gray',fg='white',font=('arial',10),width=15,height=2)
            l5.place(x=170,y=280)
            bt17=Button(c,text='insert',bg='black',fg='white',width=10,font=10,command=batchdatainsert)
            bt17.place(x=170,y=330,height=40)
            bt18=Button(c,text='find',bg='black',fg='white',width=10,font=10,command=batchdatafind)
            bt18.place(x=170,y=370,height=40)
            bt19=Button(c,text='update',bg='black',fg='white',width=10,font=10,command=batchdataupdate)
            bt19.place(x=170,y=410,height=40)
            bt20=Button(c,text='delete',bg='black',fg='white',width=10,font=10,command=batchdatadelete)
            bt20.place(x=170,y=450,height=40)
            
            l6=Label(c,text='Batch_Shift',bg='gray',fg='white',font=('arial',10),width=15,height=2)
            l6.place(x=320,y=280)
            bt21=Button(c,text='insert',bg='black',fg='white',width=10,font=10,command=batchshiftinsert)
            bt21.place(x=320,y=330,height=40)
            bt22=Button(c,text='find',bg='black',fg='white',width=10,font=10,command=batchshiftfind)
            bt22.place(x=320,y=370,height=40)
            bt23=Button(c,text='update',bg='black',fg='white',width=10,font=10)
            bt23.place(x=320,y=410,height=40)
            bt24=Button(c,text='delete',bg='black',fg='white',width=10,font=10)
            bt24.place(x=320,y=450,height=40)
            
            l7=Label(c,text='Course_Details',bg='gray',fg='white',font=('arial',10),width=15,height=2)
            l7.place(x=100,y=520)
            bt25=Button(c,text='insert',bg='black',fg='white',width=10,font=10,command=courseinsert)
            bt25.place(x=100,y=570,height=40)
            bt26=Button(c,text='find',bg='black',fg='white',width=10,font=10,command=coursefind)
            bt26.place(x=100,y=610,height=40)
            bt27=Button(c,text='update',bg='black',fg='white',width=10,font=10,command=courseupdate)
            bt27.place(x=100,y=650,height=40)
            bt28=Button(c,text='delete',bg='black',fg='white',width=10,font=10,command=coursedelete)
            bt28.place(x=100,y=690,height=40)
            
            
            
            l9=Label(c,text='Fee_Plan',bg='gray',fg='white',font=('arial',10),width=15,height=2)
            l9.place(x=250,y=520)
            bt33=Button(c,text='insert',bg='black',fg='white',width=10,font=10,command=feeplaninsert)
            bt33.place(x=250,y=570,height=40)
            bt34=Button(c,text='find',bg='black',fg='white',width=10,font=10,command=feeplanfind)
            bt34.place(x=250,y=610,height=40)
            bt35=Button(c,text='update',bg='black',fg='white',width=10,font=10,command=feeplanupdate)
            bt35.place(x=250,y=650,height=40)
            bt36=Button(c,text='delete',bg='black',fg='white',width=10,font=10,command=feeplandelete)
            bt36.place(x=250,y=690,height=40)
            #t.mainloop()

           
        elif ps!=data[0]:
            messagebox.showinfo("error","invalid password..")
        
        else:
             messagebox.showinfo("error","wrong id or password..")
             
    c=Canvas(width=900,height=1000,bg='sky blue')
    c.place(x=650,y=0)
    f=Frame(c,bg='white')
    f.place(x=180,y=140,width=500,heigh=380)
    l1=Label(f,text="Admin login Here",font=('impact',28,'bold'),width=20,height=2,bg='white',fg='black')
    l1.place(x=10,y=10)
    u=Label(f,text='Admin Id',font=('lucida handwriting',16),bg='white',fg='blue')
    u.place(x=50,y=110)
    e1=ttk.Combobox(f,width=48)
    e1.place(x=50,y=160,height=30)
    data=filldatatwo()
    e1['values']=data
    #password=StringVar()
    p=Label(f,text='Password',font=('lucida handwriting',16),bg='white',fg='blue')
    p.place(x=50,y=200)
    e2=Entry(f,width=50,bg='light gray',show='*')
    e2.place(x=50,y=250,height=30)
    b1=Button(c,text="Login",width=10,height=2,font=10,bg='light blue',fg='black',command=pas)
    b1.place(x=250,y=480)
    b2=Button(c,text="Cancel",width=10,height=2,font=10,bg='light blue',fg='black')
    b2.place(x=480,y=480)
    
'''bt=Button(t,text="save",command=Alogin)
bt.place(x=50,y=50)
t.mainloop()'''