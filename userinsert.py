import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def userinsert():
    def insertuser():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=e1.get()
        y=e2.get()
        z=e3.get()
        #q=e4.get()
        u=e5.get()
        w=e6.get()
        s="insert into user values('%s','%s','%s','%s','%s')"%(x,y,z,u,w)
        cur.execute(s)
        db.commit()
        messagebox.showinfo("Data Saved","Saved...")
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        #cb1.delete(0,100)
        e6.delete(0,100)
        db.close()
    def validatepass():
        if ep.get()==cp.get():
            messagebox.showinfo("confimed","password confirmed...")
        else:
            messagebox.showinfo("confimed","password Not confirmed...")
         
    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    
    '''im=PhotoImage(file='aa.gif')
    c.create_image(500,0,image=im)'''
    
   
    #bg = PhotoImage(file='aa.gif')
    #label1 = Label(c, image = bg)
    #label1.place(x = 0, y = 0)
    
    a=Label(c,text="User Registration",font=('Bookman Old Style',20),width=23,height=2)
    a.place(x=350,y=70)
    l1=Label(c,text="User Id",font=('TimesNewRoman'),width=15)
    l1.place(x=50,y=200)
    e1=Entry(c,width=30)
    e1.place(x=300,y=200,height=30)
    l2=Label(c,text="User Name",font=('TimesNewRoman'),width=15)
    l2.place(x=600,y=200)
    e2=Entry(c,width=30)
    e2.place(x=800,y=200,height=30)
    l3=Label(c,text="Password",font=('TimesNewRoman'),width=15)
    l3.place(x=50,y=300)
    ep=StringVar()
    e3=Entry(c,width=30,textvariable=ep,show='*')
    e3.place(x=300,y=300,height=30)
    l4=Label(c,text="Confirm Password",font=('TimesNewRoman'),width=15)
    l4.place(x=600,y=300)
    cp=StringVar()
    e4=Entry(c,width=30,textvariable=cp,show='*')
    e4.place(x=800,y=300,height=30)
    #validatepass=partial(validatepass,ep,cp)
    bt3=Button(text="check",command=validatepass)
    bt3.place(x=800,y=350)
    l5=Label(c,text="Email",font=('TimesNewRoman'),width=15)
    l5.place(x=50,y=400)
    e5=Entry(c,width=30)
    e5.place(x=300,y=400,height=30)
    l6=Label(c,text="Phone no",font=('TimesNewRoman'),width=15)
    l6.place(x=600,y=400)
    e6=Entry(c,width=30)
    e6.place(x=800,y=400,height=30)
    bt1=Button(c,text="save",font=('Bookman Old Style',20),width=8,command=insertuser)
    bt1.place(x=350,y=550)
    bt2=Button(c,text="Cancel",font=('Bookman Old Style',20),width=8)
    bt2.place(x=550,y=550)