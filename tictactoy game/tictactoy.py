from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

#Global Variable
ActivePlayer=1
p1=[]
p2=[]

root=Tk()
root.title("Tic Tac Toy Game : Player 1")
style=ttk.Style()
style.theme_use('classic')
style.configure('TButton', font= 40)
#Adding The buttons with a specific ID

bu1=ttk.Button(root, text=" ")
bu1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
bu1.config(command=lambda: BuClick(1))

bu2=ttk.Button(root, text=" ")
bu2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
bu2.config(command=lambda: BuClick(2))

bu3=ttk.Button(root, text=" ")
bu3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
bu3.config(command=lambda: BuClick(3))

bu4=ttk.Button(root, text=" ")
bu4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
bu4.config(command=lambda: BuClick(4))

bu5=ttk.Button(root, text=" ")
bu5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
bu5.config(command=lambda: BuClick(5))

bu6=ttk.Button(root, text=" ")
bu6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
bu6.config(command=lambda: BuClick(6))

bu7=ttk.Button(root, text=" ")
bu7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
bu7.config(command=lambda: BuClick(7))

bu8=ttk.Button(root, text=" ")
bu8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
bu8.config(command=lambda: BuClick(8))

bu9=ttk.Button(root, text=" ")
bu9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
bu9.config(command=lambda: BuClick(9))

def BuClick(ID):

    global ActivePlayer
    global p1
    global p2

    if (ActivePlayer==1):
        SetLayout(ID, "X")
        p1.append(ID)
        root.title("Tic Tac Toy Game : Player 2")
        ActivePlayer=2
        print("P1 : {}".format(p1))
        #Autoplay()

    elif (ActivePlayer==2):
        SetLayout(ID, "O")
        p2.append(ID)
        root.title("Tic Tac Toy Game : Player 1")
        ActivePlayer=1
        print("P2 : {}".format(p2))
        

    CheckWinner()
    Autoplay()



def SetLayout(ID, PlayerSymbol):
    
    if (ID==1):
        bu1.config(text=PlayerSymbol)
        bu1.state(['disabled'])

    elif (ID==2):
        bu2.config(text=PlayerSymbol)
        bu2.state(['disabled'])

    elif (ID==3):
        bu3.config(text=PlayerSymbol)
        bu3.state(['disabled'])

    elif (ID==4):
        bu4.config(text=PlayerSymbol)
        bu4.state(['disabled'])

    elif (ID==5):
        bu5.config(text=PlayerSymbol)
        bu5.state(['disabled'])

    elif (ID==6):
        bu6.config(text=PlayerSymbol)
        bu6.state(['disabled'])

    elif (ID==7):
        bu7.config(text=PlayerSymbol)
        bu7.state(['disabled'])
    
    elif (ID==8):
        bu8.config(text=PlayerSymbol)
        bu8.state(['disabled'])

    elif (ID==9):
        bu9.config(text=PlayerSymbol)
        bu9.state(['disabled'])

def CheckWinner():
    Winner=-1
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        Winner=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        Winner=2

    if ((4 in p1) and (5 in p1) and (6 in p1)):
        Winner=1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Winner=2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        Winner=1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        Winner=2
    
    #Checking Winner by column

    if ((1 in p1) and (4 in p1) and (7 in p1)):
        Winner=1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        Winner=2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        Winner=1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        Winner=2

    if ((3 in p1) and (6 in p1) and (9 in p1)):
        Winner=1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        Winner=2

    # Checking Winner diagonally

    if ((1 in p1) and (5 in p1) and (9 in p1)):
        Winner=1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        Winner=2    

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        Winner=1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        Winner=2

    if (Winner==1):
        messagebox.showinfo(title="Congratulations", message="Player 1 is the winner")
        #Autoplay()
    elif (Winner==2):
        messagebox.showinfo(title="Congratulations", message="Player 2 is the winner")
        #Autoplay()


def Autoplay():
    global p1
    global p2
    EmptyCells=[]
    ID=[1,2,3,4,5,6,7,8,9]

    for cell in range(9):
        if (not(cell+1 in p1) or (cell+1 in p2)):   # I used +1 because range start from 0
            EmptyCells.append(cell+1)
            #ClearWindow(EmptyCells[cell+1])     
    RandIndex=randint(0, len(EmptyCells)-1) 
    BuClick(EmptyCells[RandIndex])


"""
def ClearWindow(ID):
    #TButton.state(['disabled'])
    
    if (ID==1):
        bu1.state(['disabled'])
    if (ID==2):
        bu2.state(['disabled'])
    if (ID==3):
        bu3.state(['disabled'])
    if (ID==4):
        bu4.state(['disabled'])
    if (ID==5):
        bu5.state(['disabled'])
    if (ID==6):
        bu6.state(['disabled'])
    if (ID==7):
        bu7.state(['disabled'])
    if (ID==8):
        bu8.state(['disabled'])
    if (ID==9):
        bu9.state(['disabled'])
"""
root.mainloop()