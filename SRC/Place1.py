from tkinter import *

bs=Tk()
bs.geometry("400x600")
a=Label(bs,text="Username").place(x=30,y=50)
e1=Entry(bs).place(x=100,y=50)
b=Label(bs,text="Password").place(x=30,y=90)
e2=Entry(bs).place(x=100,y=100)
c=Button(bs,text="Login").place(x=150,y=170)
d=Button(bs,text="Sign In").place(x=150,y=200)
e=Label(bs,text="Forget Password?").place(x=150,y=230)

bs.mainloop()