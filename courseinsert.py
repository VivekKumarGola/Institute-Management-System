import tkinter
import pymysql
from tkinter import messagebox
from tkinter import *
#t=tkinter.Tk()
#t.geometry('1700x1700')
def courseinsert():
    def insertdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='institution')
            cur=db.cursor()
            x=e1.get()
            y=e2.get()
            z=e3.get()
            q=int(e4.get())
            s="insert into course values('%s','%s','%s',%d)"%(x,y,z,q)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Data Saved","Saved...")
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            db.close()
    def dele():
        c.destroy()
    
    

    c=Canvas(width=1700,height=1700,bg='pink')
    c.place(x=500,y=0)
    
    
    #bg = PhotoImage(file='bb.gif')
    #label1 = Label(c,image = bg)
    #label1.place(x = 0, y = 0)

    
    
    a=Label(c,text="Course",font=('Bookman Old Style',20),width=23,height=2)
    a.place(x=350,y=70)
    l1=Label(c,text="Course Id",font=('TimesNewRoman'),width=15)
    l1.place(x=50,y=200)
    e1=Entry(c,width=30)
    e1.place(x=300,y=200,height=30)
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
    
    bt1=Button(c,text="save",font=('Bookman Old Style',20),width=8,command=insertdata)
    bt1.place(x=350,y=550)
    bt2=Button(c,text="Cancel",font=('Bookman Old Style',20),width=8,command=dele)
    bt2.place(x=550,y=550)
