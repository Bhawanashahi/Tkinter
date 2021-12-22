from tkinter import *

Bhawana=Tk()
User=Label(Bhawana,text="Fullname")
User.pack()
e1=Entry(Bhawana).pack()
Username=Label(Bhawana,text="Username")
Username.pack()
e2=Entry(Bhawana).pack()
email=Label(Bhawana,text="Email")
email.pack()
e3=Entry(Bhawana).pack()
Password=Label(Bhawana,text="Password")
Password.pack()
e4=Entry(Bhawana).pack()
Register=Button(Bhawana,text="Register")
Register.pack()

Bhawana.mainloop()