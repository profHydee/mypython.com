import sqlite3

class MyDatabase:
    def __init__(self):
        self._deebee=sqlite3.connect("StaffRecord.db")
        self._deebee.row_factory=sqlite3.Row
        self._deebee.execute("create table if not exists StaffLogin(ID integer primary key autoincrement, Name Text, Password Text)")
        self._deebee.commit()
    """
    deebee=sqlite3.connect("StaffRecord.db")
    deebee.row_factory=sqlite3.Row
    deebee.execute("create table if not exists StaffLogin(ID integer primary key autoincrement, Name Text, Password Text)")
    deebee.commit()
    """

    def SignUp(self,Name, Password):
        self._deebee.row_factory=sqlite3.Row
        self._deebee.execute("insert into StaffLogin(Name, Password) values(?,?)", (Name, Password))
        self._deebee.commit()
        return ("Your record has been added, Welcome!!!")
    
    def Login(self,Name, Password):
        try:
            getInfo=self._deebee.execute("select * from StaffLogin")
            names=[]
            password=[]
            #i=len(names)
            #i=names.index(Name)
            #j=password.index(Password)
            
            for row in getInfo:
                names.append(row["Name"])
                password.append(row["Password"])
            i=names.index(Name)
            j=password.index(Password)
            print(names)
            print(password)
            #if ((Name in names) and (Password in password)):
       
            if i==j:
                return ("welcome {}".format(Name))
        except:
            return ("Wrong Username or password, Try Again")
        #else:
        #if not((Name in names) and (Password in password)):
            #return ("Invalid Login, Try Again")
            
    """
    def Login(self,Name, Password):
        getInfo=self._deebee.execute("select * from StaffLogin")
        for row in getInfo:
            #print(names)
            pass
            if ((Name in row["Name"]) and (Password in row["password"])):
                return ("welcome")
            else:
                return ("Invalid Login, try Again")
"""
    def ListStaffs(self):
        listing=self._deebee.execute("select * from StaffLogin")
        for get in listing:
            print("ID : {} *** Name : {} *** Password : {}".format(get["ID"],get["Name"], get["Password"]))

    def ChangePassword(self, Name, Password, ConfirmPassword):
        self._deebee.row_factory=sqlite3.Row
        flag=0
        if (Password == ConfirmPassword):
            self._deebee.execute("update StaffLogin set Password=? where Name=?", (Password, Name))
            self._deebee.commit()
            flag=1
        #return ("Login Details Updated")        
        else:
            return ("Password not equal, Try Again")
        if flag ==1:
            return("Password Changed Successfully")
        
        
        
        


"""
def main():
    mydata=MyDatabase()
    while 1:  
        OpEntry=input( "***\n Please Select the operation you which to perform\n ***""\n1. Sign Up \n 2. Sign In \n 3. Retrieve Password\n 4. List Staff\n""Enter Option here ")
      
        if (OpEntry== "1"):

            YourName=input("Enter Your Name Here")
            Password=input("Enter our secret Pin")
            mydata.SignUp(YourName, Password)
        elif (OpEntry=="2"):
            Name=input("Name")
            Password=input("Password")
            mydata.Login(Name,Password)
        elif (OpEntry=="3"):
            Name=input("Enter You Name")
            Password=input("Enter New Password")
            ConfirmPassword=input("Enter new password again")
            if (Password == ConfirmPassword):
                mydata.ChangePassword(Name, Password)
                    
            else:
                print("Password not equal, Try Again")
                exit
                

        elif (OpEntry=="4"):
            mydata.ListStaffs()    
        else:
            print("Something is wrong")

if __name__=="__main__": main()
           """
        