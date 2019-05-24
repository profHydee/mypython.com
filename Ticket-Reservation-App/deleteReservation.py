from tkinter import *
from tkinter import ttk
from Mydatabase import MyReservation
from tkinter import messagebox


class DeleteTickets:

    def __init__(self):
        self._myreservation=MyReservation()
        self._root=Tk()
        self._root.title("Delete Reservation")

        #Adding the entry field for data needed to delete a ticket

        ttk.Label(self._root, text="Please Enter the details below to delete your reservation").grid(row=0, column=0, columnspan=3, pady=8, padx=8, sticky="w")
        ttk.Label(self._root, text="ID").grid(row=1, column=0, sticky="e")
        
        IdEntry=ttk.Entry(self._root, width=30)
        IdEntry.grid(row=1, column=1)

        DelButton=ttk.Button(self._root, text="Delete Ticket")
        DelButton.grid(row=2, column=1)

        def BuClick():
            #print("hope it works")
            msg=self._myreservation.DeleteMyTickets(IdEntry.get())
            messagebox.showinfo(title="Delete Reservation", message=msg)
            IdEntry.delete(0, 'end')
                    
        DelButton.config(command=BuClick)
        self._root.mainloop()

