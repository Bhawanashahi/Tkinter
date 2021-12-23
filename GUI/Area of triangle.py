from tkinter import *

bs=Tk()
r=Label(bs,text="Radius of circle")
r.grid(row=0,column=0)
e=Entry(bs).grid(row=0,column=1)
b=Button(bs,text="22/7* a^2")
b.grid(row=0,column=1)
c=Label(bs,text="Area of circle")
c=Entry(bs).grid(row=2,column=2)
bs.mainloop()
