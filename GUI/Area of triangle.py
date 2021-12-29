from tkinter import*

bs=Tk()
a=Label(bs,text="Enter a base of triangle")
a.grid(row=0,column=0)
e=Entry(bs).grid(row=0,column=1)
b=Label(bs,text="Enter a height of a triangle")
b.grid(row=1,column=0)
e1=Entry(bs).grid(row=1,column=1)
c=Button(bs,text="Area of triangle=1/2*a*b")
c.grid(row=3,column=1)
d=Label(bs,text="Result")
d.grid(row=6,column=0)
e2=Entry(bs).grid(row=6,column=1)

bs.mainloop()