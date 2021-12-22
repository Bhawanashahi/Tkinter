from  tkinter import *

bs=Tk()
a=Label(bs,text="Username")
a.pack()
e1=Entry(bs).pack()
b=Label(bs,text="Password")
b.pack()
e2=Entry(bs).pack()
c=Button(bs,text="Login")
c.pack()
d=Button(bs,text="Sign In")
d.pack()
e=Label(bs,text="Froget Password")
e.pack()

bs.mainloop()
