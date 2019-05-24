from tkinter import *
from tkinter import ttk
from Mydatabase import MyReservation
from tkinter import messagebox


class UpdateTicket:
    def __init__(self):
        self._myreservation=MyReservation()
        self._root=Tk()
        self._root.title("UpdateReservation")

        #Adding Label

        ttk.Label(self._root, text="Please Enter the details of the ticket to be deleted").grid(row=0,column=0,pady=8)
        ttk.Label(self._root, text="Enter ID").grid(row=1,column=0,pady=8)
        ttk.Label(self._root, text="Enter New Emails").grid(row=2,column=0,pady=8)


        #Adding Entry
        IdEntry=ttk.Entry(self._root, width=30)
        IdEntry.grid(row=1,column=1,pady=5,padx=5)

        EmailEntry=ttk.Entry(self._root, width=30)
        EmailEntry.grid(row=2,column=1,pady=5, padx=5)
        #Adding Buttom

        UpdateButton=ttk.Button(self._root, text="Update Reservation")
        UpdateButton.grid(row=3, column=0, pady=8)

        def UpdateClick():
            msg=self._myreservation.UpdateMyTickets(IdEntry.get(), EmailEntry.get())
            messagebox.showinfo(title="Update Ticket", message=msg)

        UpdateButton.config(command=UpdateClick)
        self._root.mainloop()