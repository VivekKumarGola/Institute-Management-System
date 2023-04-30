import tkinter
import pymysql
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def enquiryfind():
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=cb1.get()
        s="select name,address,email,phoneno,dob,qualification,dateofenquiry,course_id,nextvisitdate from enquiry where enquiry_id='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        e8.insert(0,data[6])
        e9.insert(0,data[7])
        e10.insert(0,data[8])
         
    def cl():
        cb1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        e9.delete(0,100)
        e10.delete(0,100)
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select enquiry_id from enquiry" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def dele():
        c.destroy()
        
    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    a=Label(c,text="Enquiry",font=('Bookman Old Style',20),width=23,height=2)
    a.place(x=350,y=70)
    
    l1=Label(c,text="Enquiry Id",font=('TimesNewRoman'),width=15)
    l1.place(x=50,y=200)
    cb1=ttk.Combobox()
    data=filldata()
    cb1['values']=data
    cb1.place(x=800,y=200,height=30,width=185)
    
    l2=Label(c,text="Name",font=('TimesNewRoman'),width=15)
    l2.place(x=600,y=200)
    e2=Entry(c,width=30)
    e2.place(x=800,y=200,height=30)
    
    l3=Label(c,text="Address",font=('TimesNewRoman'),width=15)
    l3.place(x=50,y=300)
    e3=Entry(c,width=30)
    e3.place(x=300,y=300,height=30)
    
    l4=Label(c,text="Email",font=('TimesNewRoman'),width=15)
    l4.place(x=600,y=300)
    e4=Entry(c,width=30)
    e4.place(x=800,y=300,height=30)
    
    l5=Label(c,text="Phone no",font=('TimesNewRoman'),width=15)
    l5.place(x=50,y=400)
    e5=Entry(c,width=30)
    e5.place(x=300,y=400,height=30)
    
    l6=Label(c,text="D.O.B",font=('TimesNewRoman'),width=15)
    l6.place(x=600,y=400)
    e6=Entry(c,width=30)
    e6.place(x=800,y=400,height=30)
    
    l7=Label(c,text="Qualification",font=('TimesNewRoman'),width=15)
    l7.place(x=50,y=500)
    e7=Entry(c,width=30)
    e7.place(x=300,y=500,height=30)
    
    l8=Label(c,text="Date of Enquiry",font=('TimesNewRoman'),width=15)
    l8.place(x=600,y=500)
    e8=Entry(c,width=30)
    e8.place(x=800,y=500,height=30)
    
    l9=Label(c,text="Coures Id ",font=('TimesNewRoman'),width=15)
    l9.place(x=50,y=600)
    e9=Entry(c,width=30)
    e9.place(x=300,y=600,height=30)
    
    l10=Label(c,text="Next Visit date",font=('TimesNewRoman'),width=15)
    l10.place(x=600,y=600)
    e10=Entry(c,width=30)
    e10.place(x=800,y=600,height=30)
        
    bt1=Button(c,text="Find",font=('Bookman Old Style',20),width=8,command=finddata)
    bt1.place(x=350,y=700)
    bt2=Button(c,text="New Find",font=('Bookman Old Style',20),width=8,command=cl)
    bt2.place(x=550,y=700)
    

    
