import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
#t=tkinter.Tk()#make tkinter
#t.geometry('1700x1700')
def batchshiftfind():
    def batchshiftf():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
        cur=db.cursor()
        x=e1.get()
        s2="select mon,tue,wed,thu,fri,sat,sun from batch_shift where batchshift_id='%s'"%(x)
        cur.execute(s2)
        data=cur.fetchone()
        m.delete(0,100)
        tu.delete(0,100)
        w.delete(0,100)
        th.delete(0,100)
        f.delete(0,100)
        sa.delete(0,100)
        su.delete(0,100)
        m.insert(0,data[0])
        tu.insert(0,data[1])
        w.insert(0,data[2])
        th.insert(0,data[3])
        f.insert(0,data[4])
        sa.insert(0,data[5])
        su.insert(0,data[6])
        db.close()
    def filldatatwo():
            db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
            cur=db.cursor()
            x=[]
            s="select batchshift_id from batch_shift"
            cur.execute(s)
            data=cur.fetchall()
            for res in data:
                x.append(res[0])
            return(x)

    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    a=Label(c,text="Batch Shift Details",font=('Bookman Old Style',20),width=25,height=3)
    a.place(x=350,y=70)
    l1=Label(c,text="Batch Shift Id",font=('TimesNewRoman'),width=15)
    l1.place(x=400,y=230)
    e1=ttk.Combobox(c,width=30)
    e1.place(x=600,y=230,height=30)
    data=filldatatwo()
    e1['values']=data
    m=IntVar()
    tu=IntVar()
    w=IntVar()
    th=IntVar()
    f=IntVar()
    sa=IntVar()
    su=IntVar()
    c1=Checkbutton(c,text='Monday',font=('TimesNewRoman'),width=10,variable=m,onvalue=1,offvalue=0)
    c1.place(x=500,y=300)
    c2=Checkbutton(c,text='Tuesday',font=('TimesNewRoman'),width=10,variable=tu,onvalue=1,offvalue=0)
    c2.place(x=500,y=360)
    c3=Checkbutton(c,text='Wednesday',font=('TimesNewRoman'),width=10,variable=w,onvalue=1,offvalue=0)
    c3.place(x=500,y=420)
    c4=Checkbutton(c,text='Thursday',font=('TimesNewRoman'),width=10,variable=th,onvalue=1,offvalue=0)
    c4.place(x=500,y=480)
    c5=Checkbutton(c,text='Friday',font=('TimesNewRoman'),width=10,variable=f,onvalue=1,offvalue=0)
    c5.place(x=500,y=540)
    c6=Checkbutton(c,text='Saturday',font=('TimesNewRoman'),width=10,variable=sa,onvalue=1,offvalue=0)
    c6.place(x=500,y=600)
    c7=Checkbutton(c,text='Sunday',font=('TimesNewRoman'),width=10,variable=su,onvalue=1,offvalue=0)
    c7.place(x=500,y=660)

    bt1=Button(c,text="Find",font=('Bookman Old Style',20),width=8,command=batchshiftf)
    bt1.place(x=300,y=680)
    
    bt3=Button(c,text="Close",font=('Bookman Old Style',20),width=8)
    bt3.place(x=700,y=680)
    
