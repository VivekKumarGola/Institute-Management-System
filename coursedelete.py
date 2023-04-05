import tkinter
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
def coursedelete():
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=cb1.get()
        s="select cname,duration_days,total_fee from course where course_id='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select course_id from course" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x

    def deletedata():
         db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
         cur=db.cursor()
         x=cb1.get()
         s="delete  from course where course_id='%s'"%(x)
         cur.execute(s)
         db.commit()
         messagebox.showinfo("Data Delete","Deleted..")
         cb1.delete(0,100)
         e2.delete(0,100)
         e3.delete(0,100)
         e4.delete(0,100)
         db.close()
         
    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    a=Label(c,text="Course",font=('Bookman Old Style',20),width=23,height=2)
    a.place(x=350,y=70)
    
    l1=Label(c,text="Course Id",font=('TimesNewRoman'),width=15)
    l1.place(x=50,y=200)
    cb1=ttk.Combobox()
    data=filldata()
    cb1['values']=data
    cb1.place(x=800,y=200,height=30,width=180)
    
    l2=Label(c,text="Course Name",font=('TimesNewRoman'),width=15)
    l2.place(x=600,y=200)
    e2=Entry(c,width=30)
    e2.place(x=800,y=200,height=30)
    l3=Label(c,text="Duration",font=('TimesNewRoman'),width=15)
    l3.place(x=50,y=300)
    e3=Entry(c,width=30)
    e3.place(x=300,y=300,height=30)
    l4=Label(c,text="Total fees",font=('TimesNewRoman'),width=15)
    l4.place(x=600,y=300)
    e4=Entry(c,width=30)
    e4.place(x=800,y=300,height=30)
    
    bt1=Button(c,text="Find",font=('Bookman Old Style',20),width=8,command=finddata)
    bt1.place(x=350,y=550)
    bt2=Button(c,text="Delete",font=('Bookman Old Style',20),width=8,command=deletedata)
    bt2.place(x=550,y=550)
    
    