from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Mydatabase import MyReservation


class ListTickets:
    def __init__(self):
        self._reserve=MyReservation()
        self._root=Tk()
        self._root.title("My Reservations")
        tv=ttk.Treeview(self._root)
        tv.pack()

        tv.heading('#0',text="ID")
        tv.configure(column=('Name','Phone', 'Email', 'Gender', 'Comment', 'Profession'))
        tv.heading('Name', text="Name")
        tv.heading('Phone',text="Phone")
        tv.heading('Email', text="Email")
        tv.heading('Gender',text="Gender")
        tv.heading('Comment', text="Comment")
        tv.heading('Profession', text="Profession")
        tv.column('Name', anchor='center')
        tv.column('Phone', anchor='center')
        tv.column('Email', anchor='center')
        tv.column('Gender', anchor='center')
        tv.column('Comment', anchor='center')
        tv.column('Profession', anchor='center')

        getRow = self._reserve.ListMyTickets()
        for row in getRow:
            tv.insert('', 'end', '#{}'.format(row["ID"]), text= row["ID"])
            tv.set("#{}".format(row["ID"]), 'Name', row['Name'] )     #Set each column of the database to be equal to its respective column on tree view
            tv.set("#{}".format(row["ID"]), 'Phone',row['Phone'])
            tv.set("#{}".format(row["ID"]), 'Email', row['Email'])
            tv.set("#{}".format(row["ID"]), 'Gender', row['Gender'])
            tv.set("#{}".format(row["ID"]), 'Comment', row['Comment'])
            tv.set("#{}".format(row["ID"]), 'Profession', row['Profession'])

        self._root.mainloop()


        