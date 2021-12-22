from tkinter import *

bs=Tk()
bs.geometry("400x600")
a=Label(bs,text="Fullname").place(x=30,y=50)
e1=Entry(bs).place(x=100,y=60)
b=Label(bs,text="Username").place(x=30,y=90)
e2=Entry(bs).place(x=100,y=100)
c=Label(bs,text="Email").place(x=30,y=130)
e3=Entry(bs).place(x=100,y=140)
d=Label(bs,text="Password").place(x=30,y=170)
e4=Entry(bs).place(x=100,y=180)
e=Button(bs,text="Register").place(x=200,y=250)

bs.mainloop()