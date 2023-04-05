import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def userlogin():
    def filldatatwo():
         db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
         cur=db.cursor()
         x=[]
         s="select user_id from user "
         cur.execute(s)
         data=cur.fetchall()
         for res in data:
             x.append(res[0])
         return(x)
    def Uloginscreen():
         db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
         cur=db.cursor()
         
         x=e1.get()
         ps=e2.get()
         s="select password from user where user_id='%s'"%(x)
         cur.execute(s)
         data=cur.fetchone()
         
         if ps=="" and x=="":
             messagebox.showinfo("error","fill id or password..")
         elif ps=="":
             messagebox.showinfo("error","fill required password..")
         elif x=="":
             messagebox.showinfo("error","fill required id..")
         elif ps==data[0]:
             messagebox.showinfo("error","Login Successful..")
         elif ps!=data[0]:
             messagebox.showinfo("error","invalid password..")
         
         else:
              messagebox.showinfo("error","wrong id or password..")
    c=Canvas(width=900,height=1000,bg='light pink')
    c.place(x=650,y=0)
    
     
    f=Frame(c,bg='white')
    f.place(x=180,y=140,width=500,heigh=380)
    l1=Label(f,text="User login Here",font=('impact',28,'bold'),width=20,height=2,bg='white',fg='black')
    l1.place(x=10,y=10)
    u=Label(f,text='User Id',font=('lucida handwriting',16),bg='white',fg='black')
    u.place(x=50,y=110)
    e1=ttk.Combobox(f,width=48)
    e1.place(x=50,y=160,height=30)
    data=filldatatwo()
    e1['values']=data
    #password=StringVar()
    p=Label(f,text='Password',font=('lucida handwriting',16),bg='white',fg='black')
    p.place(x=50,y=200)
    e2=Entry(f,width=50,bg='light gray',show='*')
    e2.place(x=50,y=250,height=30)
    b1=Button(c,text="Login",width=10,height=2,font=10,bg='gray',fg='black',command=Uloginscreen)
    b1.place(x=250,y=480)
    b2=Button(c,text="Cancel",width=10,height=2,font=10,bg='gray',fg='black',command=c.destroy)
    b2.place(x=480,y=480)