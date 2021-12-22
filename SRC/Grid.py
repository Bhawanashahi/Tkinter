from tkinter import *

Bhawana=Tk()
Username= Label(Bhawana,text="FullName")
Username.grid(row=0,column=0)
e1=Entry(Bhawana).grid(row=1,column=2)
Username1= Label(Bhawana,text="Username")
Username1.grid(row=1,column=0)
e2=Entry(Bhawana).grid(row=2,column=2)
email= Label(Bhawana,text="Email")
email.grid(row=2,column=0)
e3=Entry(Bhawana).grid(row=3,column=2)
password= Label(Bhawana,text="Password")
password.grid(row=3,column=0)
e4= Entry(Bhawana).grid(row=4,column=2)
Register= Button(Bhawana,text="Register")
Register.grid(row=5,column=5)

Bhawana.mainloop()

