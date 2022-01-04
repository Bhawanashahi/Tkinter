from tkinter import*

bs= Tk()
bs.title("BMI calculate")
bs.geometry("400x600")

def calculate_BMI():
    kg=float(entry_kg.get())
    height=float(entry_height.get())
    BMI=round(kg/(height**2),2)
    c['text']=f"BMI: {BMI}"

    kg=Label(bs,text="kg")
    kg.pack()
    e=Entry(bs)
    e.pack()

    height=Label(bs,text="Height")
    height.pack()
    e2=Entry(bs)
    e2.pack()

    d=Button(bs,text="calculate", command=calculate_BMI)
    d.pack()

    bs.mainloop()