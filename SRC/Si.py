from tkinter import *

bs=Tk()
bs.geometry("400x600")
a=Label(bs,text="principle Amount(Rs)").place(x=30,y=50)
e1=Entry(bs).place(x=100,y=50)
b=Label(bs,text="Rate%").place(x=30,y=70)
e2=Entry(bs).place(x=100,y=70)
c=Label(bs,text="Time(years)").place(x=30,y=90)
e3=Entry(bs).place(x=100,y=90)
d=Button(bs,text="Sumbit").place(x=80,y=120)
e=Label(bs,text="Simple interest")
e4=Entry(bs).place(x=30,y=140)
f=Button(bs,text="Add").place(x=30,y=170)
g=Button(bs,text="Subtract").place(x=70,y=170)
h=Button(bs,text="Multiply").place(x=130,y=170)
i=Button(bs,text="Division").place(x=200,y=170)
j=Label(bs,text="Result").place(x=30,y=200)
e5=Entry(bs).place(x=70,y=200)
bs.mainloop()
