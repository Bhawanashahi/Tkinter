from tkinter import *

bs=Tk()
r=Label(bs,text="Radius of circle")
r.grid(row=0,column=0)
e=Entry(bs).grid(row=0,column=1)
b=Label(bs,text="Area of circle=22/7*r^2")
b.grid(row=1,column=0)
c=Label(bs,text="Result")
c.grid(row=2,column=0)
e3=Entry(bs).grid(row=2,column=1)
bs.mainloop()

