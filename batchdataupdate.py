import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def batchdataupdate():
    def findata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=e1.get()
        s2="select batchshift_id,course_id,from_time,to_time,capacity,occupancy from batch_data where batchdata_id='%s'"%(x)
        cur.execute(s2)
        data=cur.fetchone()
        e2.delete(0,100)     
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        db.close()
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select batchdata_id from batch_data"
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return(x)
    def updatedatatwo():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=e1.get()
        y=e2.get()
        z=e3.get()
        w=e4.get()
        p=e5.get()
        r=e6.get()
        l=e7.get()
        s="update batch_data set batchshift_id='%s',course_id='%s',from_time='%s',to_time='%s',capacity='%s',occupancy='%s' where batchdata_id='%s'"%(y,z,w,p,r,l,x)
        cur.execute(s)
        db.commit()
        messagebox.showinfo("Update","update done")
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
    def filldataone():
            db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
            cur=db.cursor()
            y=[]
            s="select batchshift_id from batch_shift "
            cur.execute(s)
            data=cur.fetchall()
            for res in data:
                y.append(res[0])
            return y
    def filldatatwo():
            db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
            cur=db.cursor()
            z=[]
            s="select course_id from course"
            cur.execute(s)
            data=cur.fetchall()
            for res in data:
                z.append(res[0])
            return(z)
     
    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    a=Label(c,text="Batch Allocation",font=('Bookman Old Style',20),width=23,height=2)
    a.place(x=350,y=70)
    l1=Label(c,text="Batch Id",font=('TimesNewRoman'),width=15)
    l1.place(x=50,y=200)
    e1=ttk.Combobox(c,width=30)
    e1.place(x=300,y=200,height=30)
    data=filldata()
    e1['values']=data
    
    l2=Label(c,text="Batch Shift Id",font=('TimesNewRoman'),width=15)
    l2.place(x=600,y=200)
    e2=ttk.Combobox(c,width=30)
    e2.place(x=800,y=200,height=30)
    data=filldataone()
    e2['values']=data
    
    l3=Label(c,text="Course Id",font=('TimesNewRoman'),width=15)
    l3.place(x=50,y=300)   
    e3=ttk.Combobox(c,width=30)
    e3.place(x=300,y=300,height=30)
    data=filldatatwo()
    e3['values']=data
    
    l5=Label(c,text="from Time",font=('TimesNewRoman'),width=15)
    l5.place(x=50,y=400)
    e4=Entry(c,width=30)
    e4.place(x=300,y=400,height=30)
    l6=Label(c,text="to time",font=('TimesNewRoman'),width=15)
    l6.place(x=600,y=400)
    e5=Entry(c,width=30)
    e5.place(x=800,y=400,height=30)
    l7=Label(c,text="Capacity",font=('TimesNewRoman'),width=15)
    l7.place(x=50,y=500)
    e6=Entry(c,width=30)
    e6.place(x=300,y=500,height=30)
    l8=Label(c,text="Occupancy",font=('TimesNewRoman'),width=15)
    l8.place(x=600,y=500)
    e7=Entry(c,width=30)
    e7.place(x=800,y=500,height=30)
    
    bt1=Button(c,text="Find",font=('Bookman Old Style',20),width=8,command=findata)
    bt1.place(x=300,y=580)
    bt2=Button(c,text="Update",font=('Bookman Old Style',20),width=8,command=updatedatatwo)
    bt2.place(x=500,y=580)
    bt3=Button(c,text="Close",font=('Bookman Old Style',20),width=8)
    bt3.place(x=700,y=580)