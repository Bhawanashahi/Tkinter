from tkinter import *

bs=Tk()
a=Label(bs,text="Username")
a.grid(row=0,column=0)
e1=Entry(bs).grid(row=0,column=1)
b=Label(bs,text="Password")
b.grid(row=1,column=0)
e2=Entry(bs).grid(row=1,column=1)
c=Button(bs,text="login")
c.grid(row=4,column=1)
d=Button(bs,text="Sign In")
d.grid(row=5,column=1)
e=Label(bs,text="forget password?")
e.grid(row=6,column=1)

bs.mainloop()