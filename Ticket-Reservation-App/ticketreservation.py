from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Mydatabase import MyReservation
from Listreservation import ListTickets
from deleteReservation import DeleteTickets
from update import UpdateTicket

love=Tk()
love.title("Ticket Reservation App")
love.configure(background="#b5651d")
#changing button, label and entry background color
style=ttk.Style()
style.configure("TButton", background="#b5651d")
style.configure("TLabel", background="#b5651d")
style.configure("TEntry", background="#b5651d")
style.configure("TRadiobutton", background="#b5651d")
style.configure("TCheckbutton", background="#b5651d")
#Instance of my database Object

myreservation = MyReservation()

#Adding Labels

ttk.Label(love, text="Please fill in your information to reserve your ticket", anchor="center").grid(row=0, column=0, columnspan=2)

ttk.Label(love, text="Name").grid(row=1, column=0)
ttk.Label(love, text="Phone No").grid(row=2, column=0)
ttk.Label(love, text="Email").grid(row=4, column=0)
ttk.Label(love, text="Comment").grid(row=6, column=0)
ttk.Label(love, text="Gender").grid(row=3, column=0)
ttk.Label(love, text="Profession").grid(row=5, column=0)

#Adding Entries

NameEntry=ttk.Entry(love, width=40,)
NameEntry.grid(row=1, column=1, columnspan=2, pady=8,padx=5, sticky="w")
PhoneEntry=ttk.Entry(love, width=40)
PhoneEntry.grid(row=2, column=1,columnspan=2, pady=8,padx=5, sticky="w")
EmailEntry=ttk.Entry(love, width=40)
EmailEntry.grid(row=4, column=1, columnspan=2, pady=8,padx=5, sticky="w")
CommentEntry=Text(width=30, height=10)
CommentEntry.grid(row=6, column=1,columnspan=2, pady=8,padx=5, sticky="w")

#Adding Radiobutton and Checkbutton
gender=StringVar()
cbVar=StringVar()
cbVar1=StringVar()

gender.set("Male")
ttk.Radiobutton(love, text="Male", variable=gender, value="Male").grid(row=3, column=1,sticky="w")
ttk.Radiobutton(love, text="Female", variable=gender, value="female").grid(row=3, column=2,sticky="w")

ProffesionEntry1=ttk.Checkbutton(love, text="Web Developer")
ProffesionEntry1.grid(row=5,column=1, sticky="w")
ProffesionEntry1.config(variable=cbVar, onvalue="Yes Web dev", offvalue="No")
ProffesionEntry2=ttk.Checkbutton(love, text="Graphics designer")
ProffesionEntry2.grid(row=5,column=2)
ProffesionEntry2.config(variable=cbVar1, onvalue="Yes Graph des.", offvalue="Not at all")


#Adding Buttons
SubmitButton=ttk.Button(love, text="Submit")
SubmitButton.grid(row=7, column=0, sticky="w", ipadx=8,ipady=6)
ListButton=ttk.Button(love, text="List Reserv.")
ListButton.grid(row=7, column=1, sticky="w", ipadx=8,ipady=6)
UpdateButton=ttk.Button(love, text="Update Reserv")
UpdateButton.grid(row=7, column=2,sticky="w", ipadx=8,ipady=6)
DeleteButton=ttk.Button(love, text="Delete Reserv.")
DeleteButton.grid(row=7, column=3,sticky="w", ipadx=8,ipady=6)


def ClickSubmit():
    msg = myreservation.AddTicket(NameEntry.get(), PhoneEntry.get(), EmailEntry.get(), gender.get(), CommentEntry.get(1.0, 'end'), cbVar.get())
    messagebox.showinfo(title="Ticket Info", message=msg)
    NameEntry.delete(0, 'end')
    PhoneEntry.delete(0, 'end')
    EmailEntry.delete(0, 'end')
    CommentEntry.delete(1.0, 'end')
    #ProffesionEntry1.delete(0, 'end')

def ListClick():
    ListTickets()
    
def DelClick():
    DeleteTickets()   

def UpdateClick():
    UpdateTicket()

SubmitButton.config(command=ClickSubmit)
ListButton.config(command=ListClick)
DeleteButton.config(command=DelClick)
UpdateButton.config(command=UpdateClick)

love.mainloop()
