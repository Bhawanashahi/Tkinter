from tkinter import *

bs=Tk()
a=Button(bs,text="OFF")
a.grid(row=1,column=0)
b=Button(bs,text="ROOT")
b.grid(row=1,column=1)
c=Button(bs,text="M+")
c.grid(row=1,column=2)
d=Button(bs,text="M-")
d.grid(row=1,column=3)
e=Button(bs,text="MRC")
e.grid(row=1,column=4)
f=Button(bs,text="+/-")
f.grid(row=2,column=0)
g=Button(bs,text="7")
g.grid(row=2,column=1)
h=Button(bs,text="8")
h.grid(row=2,column=2)
i=Button(bs,text="9")
i.grid(row=2,column=3)
j=Button(bs,text="/")
j.grid(row=2,column=4)
k=Button(bs,text="%")
k.grid(row=3,column=0)
l=Button(bs,text="4")
l.grid(row=3,column=1)
m=Button(bs,text="5")
m.grid(row=3,column=2)
n=Button(bs,text="6")
n.grid(row=3,column=3)
o=Button(bs,text="X")
o.grid(row=3,column=4)
p=Button(bs,text="ON/C")
p.grid(row=4,column=0)
q=Button(bs,text="3")
q.grid(row=4,column=1)
r=Button(bs,text="2")
r.grid(row=4,column=2)
s=Button(bs,text="1")
s.grid(row=4,column=3)
t=Button(bs,text="-")
t.grid(row=4,column=4)
u=Button(bs,text="CE")
u.grid(row=5,column=0)
v=Button(bs,text="0")
v.grid(row=5,column=1)
w=Button(bs,text=".")
w.grid(row=5,column=2)
x=Button(bs,text="=")
x.grid(row=5,column=3)
y=Button(bs,text="+")
y.grid(row=5,column=4)
bs.mainloop()