from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from deebee import MyDatabase
from forget import ForgetPassword
#from TICKETreservation import BuClick

root=Tk()
root.title('***My Login Page***')
root.configure(background="#00a1ff")
style=ttk.Style()
style.configure("TLabel", background="#00a1ff")
mydata=MyDatabase()

#adding entry and label

ttk.Label(root, text="Name").grid(row=0, column=0, ipadx=10,ipady=3, padx= 40, pady=5)
NameEntry=ttk.Entry(root, width=40)
NameEntry.grid(row=0, column=1, columnspan=3, padx= 10, pady=10, ipadx=10,ipady=5)

ttk.Label(root, text="Password").grid(row= 1, column=0 , ipadx=10,ipady=3, padx= 40, pady=5)
PasswordEntry=ttk.Entry(root, width=40, show="*")
PasswordEntry.grid(row=1 , column= 1, columnspan=3, padx= 10, pady=10, ipadx=10,ipady=5)

BuReset=ttk.Button(root,text="Forget Password")
BuReset.grid(row=2, column=1 , padx= 0, pady=10,ipadx=5,ipady=5 )

BuSignup=ttk.Button(root, text="Sign Up")
BuSignup.grid(row=2, column= 2 , ipadx=5,ipady=5)

BuLogin=ttk.Button(root, text="Login")
BuLogin.grid(row=2, column= 3 , ipadx=5,ipady=5)

def SignUpClick():
    print("You clicked me")
    msg=mydata.SignUp(NameEntry.get(), PasswordEntry.get())
    NameEntry.delete(0, "end")
    PasswordEntry.delete(0,"end")
    messagebox.showinfo(title="My Login Page", message=msg)

def LoginClick():
    print("You clicked me")
    msg= mydata.Login(NameEntry.get(), PasswordEntry.get())
    messagebox.showinfo(title="My Login Page", message=msg)
    NameEntry.delete(0, "end")
    PasswordEntry.delete(0,"end")
    
    #BuClick()

def ForgetPWordClick():
    print("Olodo")
    ForgetPassword()
    
    
    #messagebox.showinfo(title="My Login Page", message=msg)

BuSignup.config(command=SignUpClick)
BuLogin.config(command=LoginClick)
BuReset.config(command=ForgetPWordClick)







root.mainloop()
