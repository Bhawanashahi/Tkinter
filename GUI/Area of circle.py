from tkinter import *

bs=Tk()
bs.title=("Area of circle")
bs.geometry("400x600")

def calculate_area():
    radius=int(entry_radius.get())
    area=22/7*radius*radius
    c['text']=f"area:{area}"

    radius=Label(bs,text="Radius").place(x=30,y=50)
    radius=Entry(bs).place(x=30,y=90)
    
    d=Button(bs,text="calculate",command=calculate_area).place(x=30,y=130)
    c=Label(bs,text="area").place(x=30,y=150)
    bs.mainloop()

