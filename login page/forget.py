from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from deebee import MyDatabase


class ForgetPassword:
    def __init__(self):

        self.mydatabase=MyDatabase()
        self.root=Tk()
        self.root.title("***Forgot Password***")
        self.root.configure(background="#efefef")

        #Adding Labels and Button

        ttk.Label(self.root, text="Please fill in the form below to reset your password").grid(row=0, column=0, columnspan=3, pady=15, sticky="snew")

        ttk.Label(self.root, text="Name").grid(row=1, column=0, pady=8, sticky="snew")
        NameEntry=ttk.Entry(self.root, width=40)
        NameEntry.grid(row=1, column=1, columnspan=2, pady=8, sticky="snew")

        ttk.Label(self.root, text="New Password").grid(row=2, column=0, pady=8, sticky="snew")
        PassEntry1=ttk.Entry(self.root, width=40, show="*")
        PassEntry1.grid(row=2, column=1, columnspan=2, pady=6, sticky="snew")

        ttk.Label(self.root, text="Confirm Password").grid(row=3, column=0, pady=8, sticky="snew")
        PassEntry2=ttk.Entry(self.root, width=40, show="*")
        PassEntry2.grid(row=3, column=1, columnspan=2, pady=6, sticky="snew")

        ForgetPasswordButton=ttk.Button(self.root, text="Change Password")
        ForgetPasswordButton.grid(row=4,column=1)

        def ForgetPasswordClick():
            #if (PassEntry1 == PassEntry1):
            msg=self.mydatabase.ChangePassword(NameEntry.get(), PassEntry1.get(), PassEntry2.get())
            messagebox.showinfo(title="Password Reset Info", message=msg)        
            #else:
                #messagebox.showinfo(title="Password Reset Info", message="Password does not match, Try Again!")
               # exit
            NameEntry.delete(0, "end")
            PassEntry1.delete(0,"end")
            PassEntry2.delete(0,"end")


        ForgetPasswordButton.config(command=ForgetPasswordClick)


        self.root.mainloop()