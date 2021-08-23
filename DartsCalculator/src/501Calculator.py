'''
Created on 21 Jan 2020

@author: lennie.flavell
'''
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.tix import COLUMN

class playersdialog(simpledialog.Dialog):
    def body(self, master):
        Label(master, text="First Player").grid(row=0)
        Label(master, text="Second Player").grid(row=1)
        
        self.player1 = Entry(master)
        self.player2 = Entry(master)
        
        self.player1.grid(row=0, column=1)
        self.player2.grid(row=1, column=1)
        return self.player1
    
    def apply(self):
        p1name = self.player1.get()
        p2 = self.player2.get()
        #print(p1,p2)
        
#p1name = input("Enter the name of player 1")
        
root = Tk()
root.withdraw()#hide the main window and just show the players name dialog entry
dialog = playersdialog(root)

root.deiconify()#show the main window after the user has entered the players name
root.geometry('400x900+0+0')

targetscore = 501
dartscore = 0
p1numberofdarts = 0
p2numberofdarts = 0
dartstofinish = 0
p1average = 0
p2average = 0
currentscorep1 = targetscore
currentscorep2 = targetscore
scorelabelnumber = 6 #variable to store the latest label used to show scores
playersturn = 1 #switch the variable from 1 to 2 once the score has been entered for player 1 then back to 1 after score entered for player 2
scoretocalculate = targetscore

#frametop = Frame(root, width=400, height=10)
#frametop.grid(row=0)

title = Label(root, text= 'Darts Calculator', font =('Times New Roman', 24))
title.grid(column=1,row=1)

targetscorelabel = Label(root, text = targetscore, font =('Times New Roman', 20)) #Enter the targetscore in this label frametop
targetscorelabel.grid(column=1,row=2)
p1label = Label(root, text = p1name, font =('Times New Roman', 20))#player1 name label
p1label.grid(column=0,row=4)
p2label = Label(root, text = 'Dom', font=('Times New Roman', 20))#player2 name label
p2label.grid(column=2,row=4)
scoreentry = Entry(root)
scoreentry.grid(column=1,row=3)
scoreentry.focus()

def calculatep1(event):
    global playersturn
    global currentscorep1
    global scorelabelnumber 
    global p1numberofdarts
    scorecheck = 0 
    dartscore = scoreentry.get()
    if currentscorep1 > 0: #calculate score if current score is greater than zero
            if (int(dartscore) ==159 or int(dartscore)==179 or int(dartscore)>180):
                messagebox.showinfo("Incorrect Score", "Please enter a correct score")#display message to user as score incorrect
            else:
                scorecheck = int(currentscorep1) - int(dartscore)#subtracts the latest score from the remaining score into a variable that can be used to check that the score is valid
                if (int(scorecheck < 0) or int(scorecheck)==1):
                    messagebox.showwarning("Bust", "You have bust your score")#the score entered is greater than the score the user has remaining
                else:
                    currentscorep1 = int(currentscorep1) - int(dartscore)    
                    scorelabel = Label(root, text = currentscorep1, font =('Times New Roman', 20))
                    scorelabel.grid(column=0,row=scorelabelnumber)
                    p1numberofdarts = int(p1numberofdarts) + 3
                    p1average = (targetscore - currentscorep1)/p1numberofdarts*3#count average as game is being played
                    scoreentry.delete(0, 'end')#remove the score from the text entry box after the calculation has been done
                    scoreentry.focus()#give the focus back to the score entry field after the score has been entered
                    playersturn=2#sets to 2 so the program calculates the second players score next
                    scorelabelnumber=scorelabelnumber + 1#increments the score label by one so that the next score will be entered on the next line if the second player has taken their turn#
                    
                    print(playersturn)
                    
                if currentscorep1==0:#game has finished
                    p1average = round(p1average,2)#round the value in the average value to 2 dp
                    lines = ['Number of darts: '+str(p1numberofdarts), 'Average: '+str(p1average)]#details for dialog to inform user game has finished
                    messagebox.showinfo("Game, Shot, Leg", "\n".join(lines))#dialog to inform user that game has finished
                    
def calculatep2(event):
    global playersturn
    global currentscorep2
    global scorelabelnumber 
    global p2numberofdarts
    scorecheck = 0 
    dartscore = scoreentry.get()
    if currentscorep2 > 0: #calculate score if current score is greater than zero
            if (int(dartscore) ==159 or int(dartscore)==179 or int(dartscore)>180):
                messagebox.showinfo("Incorrect Score", "Please enter a correct score")#display message to user as score incorrect
            else:
                scorecheck = int(currentscorep2) - int(dartscore)#subtracts the latest score from the remaining score into a variable that can be used to check that the score is valid
                if (int(scorecheck < 0) or int(scorecheck)==1):
                    messagebox.showwarning("Bust", "You have bust your score")#the score entered is greater than the score the user has remaining
                else:
                    currentscorep2 = int(currentscorep2) - int(dartscore)    
                    scorelabel = Label(root, text = currentscorep2, font =('Times New Roman', 20))
                    scorelabel.grid(column=3,row=scorelabelnumber)
                    p2numberofdarts = int(p2numberofdarts) + 3
                    p2average = (targetscore - currentscorep2)/p2numberofdarts*3#count average as game is being played
                    scoreentry.delete(0, 'end')#remove the score from the text entry box after the calculation has been done
                    scoreentry.focus()#give the focus back to the score entry field after the score has been entered
                    playersturn=1#sets to 1 so the program calculates the second players score next
                    scorelabelnumber=scorelabelnumber + 1#increments the score label by one so that the next score will be entered on the next line if the second player has taken their turn#
                    print("Inside calculatep2 function")
                    
                    
                if currentscorep2==0:#game has finished
                    p2average = round(p2average,2)#round the value in the average value to 2 dp
                    lines = ['Number of darts: '+str(p2numberofdarts), 'Average: '+str(p2average)]#details for dialog to inform user game has finished
                    messagebox.showinfo("Game, Shot, Leg", "\n".join(lines))#dialog to inform user that game has finished
            
            
if playersturn==1:
    root.bind('<Return>', calculatep1)
    print("executing calculatep1")
if playersturn==2:
    root.bind('<Return>', calculatep2)
    print("executing calculatep2")

root.mainloop()