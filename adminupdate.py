import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def adminupdate():
    def Findadmin():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=e1.get()
        s="select aname,password,aemail,aphone from admin where admin_id='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
       # e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])
       # e4.insert(0,data[2])
        e5.insert(0,data[2])
        e6.insert(0,data[3 ])
        db.close()
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

    def showpass():
        if e3.cget('show')=='*':
            e3.config(show='')
        else:
            e3.config(show='*')
            
       
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=e1.get()
        y=e2.get()
        z=e3.get()
        #w=e4.get()
        p=e5.get()
        r=e6.get()
        #l=e7.get()
        s="update admin set aname='%s',password='%s',aemail='%s',aphone='%s' where admin_id='%s'"%(y,z,p,r,x)
        cur.execute(s)
        db.commit()
        messagebox.showinfo("Update","update done")
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        #e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        #e7.delete(0,100)
       
    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    a=Label(c,text="Admin Registration",font=('Bookman Old Style',20),width=23,height=2)
    a.place(x=350,y=70)
    l1=Label(c,text="Admin Id",font=('TimesNewRoman'),width=15)
    l1.place(x=50,y=200)
    #e1=Entry(c,width=30)
    #e1.place(x=300,y=200,height=30)
    e1=ttk.Combobox(c,width=30)
    e1.place(x=300,y=200,height=30)
    data=filldatatwo()
    e1['values']=data
    l2=Label(c,text="Admin Name",font=('TimesNewRoman'),width=15)
    l2.place(x=600,y=200)
    e2=Entry(c,width=30)
    e2.place(x=800,y=200,height=30)
    l3=Label(c,text="Password",font=('TimesNewRoman'),width=15)
    l3.place(x=50,y=300)   
    e3=Entry(c,width=30,show='*')
    e3.place(x=300,y=300,height=30)
    check_button=Checkbutton(c,text="show password",command=showpass)
    check_button.place(x=500,y=300)
    l5=Label(c,text="Email",font=('TimesNewRoman'),width=15)
    l5.place(x=50,y=400)
    e5=Entry(c,width=30)
    e5.place(x=300,y=400,height=30)
    l6=Label(c,text="Phone no",font=('TimesNewRoman'),width=15)
    l6.place(x=600,y=400)
    e6=Entry(c,width=30)
    e6.place(x=800,y=400,height=30)
    bt1=Button(c,text="Find",font=('Bookman Old Style',20),width=8,command=Findadmin)
    bt1.place(x=250,y=550)
    bt2=Button(c,text="Update",font=('Bookman Old Style',20),width=8,command=updatedata)
    bt2.place(x=450,y=550)
    bt3=Button(c,text="Close",font=('Bookman Old Style',20),width=8)
    bt3.place(x=650,y=550)