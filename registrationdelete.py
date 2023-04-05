import tkinter
import pymysql
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
#t=tkinter.Tk()
#t.geometry('1700x1700')
def registrationdelete():
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=cb1.get()
        s="select enquiry_id,name,address,email,phoneno,dob,qualification,course_id,batchdata_id,batchshift_id,feeplan_id,dateoffirst_installment from registration where registration_id='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        e9.delete(0,100)
        e10.delete(0,100)
        e11.delete(0,100)
        e12.delete(0,100)
        e13.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        e8.insert(0,data[6])
        e9.insert(0,data[7])
        e10.insert(0,data[8])
        e11.insert(0,data[9])
        e12.insert(0,data[10])
        e13.insert(0,data[11])
          
    def deletedata():
         db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
         cur=db.cursor()
         x=cb1.get()
         s="delete  from registration where registration_id='%s'"%(x)
         cur.execute(s)
         db.commit()
         messagebox.showinfo("Data Delete","Deleted..")
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
         e11.delete(0,100)
         e12.delete(0,100)
         e13.delete(0,100)
         db.close()
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select registration_id from registration" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
        
    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    a=Label(c,text="Registration",font=('Bookman Old Style',20),width=23,height=2)
    a.place(x=350,y=40)
    
    l1=Label(c,text="Registration Id",font=('TimesNewRoman'),width=15)
    l1.place(x=50,y=150)
    cb1=ttk.Combobox(c,width=27)
    data=filldata()
    cb1['values']=data
    cb1.place(x=300,y=150,height=30)
    
    l2=Label(c,text="Enquiry Id",font=('TimesNewRoman'),width=15)
    l2.place(x=600,y=150)
    e2=Entry(c,width=30)
    e2.place(x=800,y=150,height=30)
    
    l3=Label(c,text="Name",font=('TimesNewRoman'),width=15)
    l3.place(x=50,y=250)
    e3=Entry(c,width=30)
    e3.place(x=300,y=250,height=30)
    
    l4=Label(c,text="Address",font=('TimesNewRoman'),width=15)
    l4.place(x=600,y=250)
    e4=Entry(c,width=30)
    e4.place(x=800,y=250,height=30)
    
    l5=Label(c,text="E mail",font=('TimesNewRoman'),width=15)
    l5.place(x=50,y=350)
    e5=Entry(c,width=30)
    e5.place(x=300,y=350,height=30)
    
    l6=Label(c,text="Phone no.",font=('TimesNewRoman'),width=15)
    l6.place(x=600,y=350)
    e6=Entry(c,width=30)
    e6.place(x=800,y=350,height=30)
    
    l7=Label(c,text="D.O.B",font=('TimesNewRoman'),width=15)
    l7.place(x=50,y=450)
    e7=Entry(c,width=30)
    e7.place(x=300,y=450,height=30)
    
    l8=Label(c,text="Qualification",font=('TimesNewRoman'),width=15)
    l8.place(x=600,y=450)
    e8=Entry(c,width=30)
    e8.place(x=800,y=450,height=30)
    
    l9=Label(c,text="Coures Id ",font=('TimesNewRoman'),width=15)
    l9.place(x=50,y=550)
    e9=Entry(c,width=30)
    e9.place(x=300,y=550,height=30)
    
    
    l10=Label(c,text="Batchdata Id",font=('TimesNewRoman'),width=15)
    l10.place(x=600,y=550)
    e10=Entry(c,width=30)
    e10.place(x=800,y=550,height=30)
    
    
    l11=Label(c,text="Batchshift Id",font=('TimesNewRoman'),width=15)
    l11.place(x=50,y=650)
    e11=Entry(c,width=30)
    e11.place(x=300,y=650,height=30)

    l12=Label(c,text="Feeplan Id",font=('TimesNewRoman'),width=15)
    l12.place(x=600,y=650)  
    e12=Entry(c,width=30)
    e12.place(x=800,y=650,height=30)

    l13=Label(c,text="Date of 1 Installment",font=('TimesNewRoman'),width=20)
    l13.place(x=50,y=725)
    e13=Entry(c,width=30)
    e13.place(x=300,y=725,height=30)
        
    bt1=Button(c,text="Find",font=('Bookman Old Style',20),width=8,command=finddata)
    bt1.place(x=550,y=725)
    bt2=Button(c,text="Delete",font=('Bookman Old Style',20),width=8,command=deletedata)
    bt2.place(x=750,y=725)
    

    