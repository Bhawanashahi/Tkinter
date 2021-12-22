from tkinter import *

Bhawana = Tk()
Bhawana.geometry("400x500")
Username = Label(Bhawana,text = "Username").place(x=30,y=50)
Password = Label(Bhawana,text ="password").place(x=30,y=90)
Username=Entry(Username).place(x=100,y=50)
Password= Entry(Password).place(x=100,y=90)
Login=Button(Bhawana,text="Login").place(x=150,y=120)
Bhawana.mainloop()

