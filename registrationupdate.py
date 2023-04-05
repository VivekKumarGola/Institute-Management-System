import tkinter
import pymysql
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
#t=tkinter.Tk()
#t.geometry('1700x1700')
def registrationupdate():
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=cb0.get()
        s="select enquiry_id,name,address,email,phoneno,dob,qualification,course_id,batchdata_id,batchshift_id,feeplan_id,dateoffirst_installment from registration where registration_id='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        cb.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        cb1.delete(0,100)
        cb2.delete(0,100)
        cb3.delete(0,100)
        cb4.delete(0,100)
        e13.delete(0,100)
        cb.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        e8.insert(0,data[6])
        cb1.insert(0,data[7])
        cb2.insert(0,data[8])
        cb3.insert(0,data[9])
        cb4.insert(0,data[10])
        e13.insert(0,data[11])
          
    def cl():
        cb0.delete(0,100)
        cb.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        cb1.delete(0,100)
        cb2.delete(0,100)
        cb3.delete(0,100)
        cb4.delete(0,100)
        e13.delete(0,100)
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        a=cb0.get()
        b=cb.get()
        c=e3.get()
        d=e4.get()
        e=e5.get()
        f=e6.get()
        g=e7.get()
        h=e8.get()
        i=cb1.get()
        j=cb2.get()
        k=cb3.get()
        l=cb4.get()
        m=e13.get()
        s="update registration set enquiry_id='%s',name='%s',address='%s',email='%s',phoneno='%s',dob='%s',qualification='%s',course_id='%s',batchdata_id='%s',batchshift_id='%s',feeplan_id='%s',dateoffirst_installment='%s' where registration_id='%s'"%(b,c,d,e,f,g,h,i,j,k,l,m,a)
        cur.execute(s)
        db.commit()
        messagebox.showinfo("Update","update done")
        db.close()
        cb0.delete(0,100)
        cb.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        cb1.delete(0,100)
        cb2.delete(0,100)
        cb3.delete(0,100)
        cb4.delete(0,100)
        e13.delete(0,100)
        
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
    
    def filldata1():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select course_id from course" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def filldata2():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select batchdata_id from batch_data" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def filldata3():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select batchshift_id from batch_shift" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def filldata4():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select feeplan_id from fee_plan" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def filldata0():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=[]
        s="select registration_id from registration" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    
    def dele():
        c.destroy()
        
    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    a=Label(c,text="Registration",font=('Bookman Old Style',20),width=23,height=2)
    a.place(x=350,y=40)
    
    l1=Label(c,text="Registration Id",font=('TimesNewRoman'),width=15)
    l1.place(x=50,y=150)
    cb0=ttk.Combobox(c,width=27)
    data=filldata0()
    cb0['values']=data
    cb0.place(x=300,y=150,height=30)
    
    l2=Label(c,text="Enquiry Id",font=('TimesNewRoman'),width=15)
    l2.place(x=600,y=150)
    cb=ttk.Combobox(c,width=27)
    data=filldata()
    cb['values']=data
    cb.place(x=800,y=150,height=30)
    
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
    cb1=ttk.Combobox(c,width=27)
    data=filldata1()
    cb1['values']=data
    cb1.place(x=300,y=550,height=30)    
    
    l10=Label(c,text="Batchdata Id",font=('TimesNewRoman'),width=15)
    l10.place(x=600,y=550)
    cb2=ttk.Combobox(c,width=27)
    data=filldata2()
    cb2['values']=data
    cb2.place(x=800,y=550,height=30)
    
    
    l11=Label(c,text="Batchshift Id",font=('TimesNewRoman'),width=15)
    l11.place(x=50,y=650)
    cb3=ttk.Combobox(c,width=27)
    data=filldata3()
    cb3['values']=data
    cb3.place(x=300,y=650,height=30)

    l12=Label(c,text="Feeplan Id",font=('TimesNewRoman'),width=15)
    l12.place(x=600,y=650)  
    cb4=ttk.Combobox(c,width=27)
    data=filldata4()
    cb4['values']=data
    cb4.place(x=800,y=650,height=30)

    l13=Label(c,text="Date of 1 Installment",font=('TimesNewRoman'),width=20)
    l13.place(x=50,y=725)
    e13=Entry(c,width=30)
    e13.place(x=300,y=725,height=30)
        
    bt1=Button(c,text="Find",font=('Bookman Old Style',20),width=8,command=finddata)
    bt1.place(x=550,y=725)
    bt2=Button(c,text="Update",font=('Bookman Old Style',20),width=8,command=updatedata)
    bt2.place(x=750,y=725)
    

    