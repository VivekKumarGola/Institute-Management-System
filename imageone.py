from tkinter import *
import tkinter 
from PIL import Image, ImageTk


width = 600
height = 600

t=tkinter.Tk() 
t.geometry('700x700') 

bg = PhotoImage(file='xyz.gif')
label1 = Label(t, image = bg)
label1.place(x = 0, y = 0)
t.title('My First Screen')

#c=Canvas(t,width=width,height=height,bg='red')

#c.pack(fill=tkinter.BOTH, expand=True)

#im=ImageTk.PhotoImage(file='xyz.gif')
#c.create_image(width,height,image=im)

t.mainloop() 