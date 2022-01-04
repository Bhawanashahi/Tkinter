#calculate the volume of cuboid

from tkinter import*
bs=Tk()
bs.title("volume of cuboid")
bs.geometry("600x400")

def calculate_volume():
    l=int(entry_length.get())
    b=int(entry_breadth.get())
    h=int(entry_height.get())
    volume=l*b*h
    c['text']=f"volume:{volume}"

    l=Label(bs,text="length")
    l.pack()
    e=Entry(bs)
    e.pack()

    b=Label(bs,text="Breadth")
    b.pack()
    e1=Entry(bs)
    e1.pack()

    h=Label(bs,text="height")
    h.pack
    e3=Entry(bs)
    e3.pack()

    c=Button(bs,text="Calulate", command="calculate_volume")
    c.pack()

    d=Label(bs,text="volume")
    d.pack()
    bs.mainloop()
