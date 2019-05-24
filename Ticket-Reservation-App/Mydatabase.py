import sqlite3

class MyReservation:
    def __init__(self):
        self._mydb=sqlite3.connect("Reservation.db")

    def create(self):
        self._mydb.row_factory=sqlite3.Row
        self._mydb.execute("create table if not exists Booking(ID integer primary key autoincrement, Name Text, Phone int, Email text, Gender text, Comment text, Profession text)")
        self._mydb.commit()

    def AddTicket(self, Name, Phone, Email, Gender, Comment, Profession):
        self._mydb.execute("insert into Booking(Name, Phone, Email, Gender, Comment, Profession) values(?,?,?,?,?,?)",(Name, Phone, Email, Gender, Comment, Profession))
        self._mydb.commit()
        return("Ticket Added Successfully")

    def ListMyTickets(self):
        self._mydb.row_factory=sqlite3.Row
        lister=self._mydb.execute(" select * from Booking")
        return(lister)
        
    def DeleteMyTickets(self, ID):
        self._mydb.row_factory=sqlite3.Row
        #self._mydb.execute("delete from Booking where ID={}".format(ID))
        self._mydb.execute("delete from Booking where ID={}".format(ID))
        self._mydb.commit()
        return("Ticket Deleted Successfully")

    def UpdateMyTickets(self,ID,Email):
        self._mydb.row_factory=sqlite3.Row
        self._mydb.execute("update Booking set Email=? where ID=?",(Email, ID))
        self._mydb.commit()
        return("Ticket Updated Successfully")

        

"""
def main():
    while 1:
        create()

        OptInput=input("*** Please select an operation to perform***\n 1. Add Ticket\n 2. List Tickets\n 3. Delete Ticket\n 4. Update Ticket\n 5. Exit\n OptSelect : ")
        
        if OptInput=="1":
            Name=input("Name")
            Phone=input("Phone")
            Email=input("Email")
            Gender=input("Gender")
            Comment=input("Comment")
            Profession=input("Profession")
            AddTicket(Name, Phone, Email, Gender, Comment, Profession)
        
        elif OptInput=="2":
            ListMyTickets()

        elif OptInput=="3":
            print("Please enter ID of the Ticket to be deleted")
            ID=int(input(" Enter ID"))
            DeleteMyTickets(ID)

        elif OptInput=="4":
            print("Please enter the details of the Ticket to be updated")
            ID=int(input(" Enter ID"))
            NewEmail=input(" Enter New Email")
            ConfirmNewEmail=input("Enter New Email Again")
            UpdateMyTickets(ID, ConfirmNewEmail)


if __name__=="__main__":main()
    """