from guizero import *
from player import Player
from game_info import Game_info

#Create the objects that are needed
game = Game_info()
p1 = Player("Player 1")
p2 = Player("Player 2")


playersturn = 1
game.set_first_throw(1)

def enter_pressed(e):#executes when enter is pressed, calculating scores and executing the main function of the app
    global playersturn
    if ord(e.key) == 13:
                print(playersturn)
                #do not calculate if score is invalid
                if (int(visitscore.value)==159 or int(visitscore.value)==179
                or int(visitscore.value)== 162 or int(visitscore.value) > 180
                or int(visitscore.value) <0):
                        print("Invalid score")
                        
                
                #calculate scores for player 1
                elif game.get_players_turn() == 1:
                    p1remscore.value = p1remscore.value[:-1]#remove the asterix from the remaining score
                    p1.calculate_score(visitscore.value, 501)
                    p1visit = p1.get_no_of_visits()
                    p1remscore.value = p1.get_remaining()                        
                    
                    if p1.get_leg_complete() != True:
                        p1.calculate_average(visitscore.value, 501, 3)#calculate player 1's average
                        p1avg.value = "Overall: " + str(p1.get_average())
                        p1100s.value = "100s :" + str(p1.get_100s())
                        p1140s.value = "140s :" + str(p1.get_140s())
                        p1180s.value = "180s :" + str(p1.get_180s())
                        p2remscore.value = p2remscore.value + "*"
                        game.set_players_turn(2)
                        if p1visit < 12 and p1.get_leg_complete() == False:#first 12 scores are placed in the left column
                            p1countdown = Text(p1scores, text=p1remscore.value, grid=[1,p1visit], size=18, align="right")
                            p1visit = Text(p1scores, text=visitscore.value, grid=[0,p1visit], size=18, align="left")
                        else:#second set of 12 scores are placed in the right column
                            p1visit = p1visit - 11
                            p1countdown = Text(p1scores, text=p1remscore.value, grid=[3,p1visit], size=18, align="right")
                            p1visit = Text(p1scores, text=visitscore.value, grid=[2,p1visit], size=18, align="left")
                            p1avg.value = "Overall: " + str(p1.get_average())
                        p1countdown.text_color = "Red"
                            
                    if p1.get_leg_complete() == True:
                        p1legslbl.value = "Legs: " +str(p1.get_legs_won())
                        darts_to_finish()

            #calculate scores for player 2
                else:
                    p2remscore.value = p2remscore.value[:-1]
                    p2.calculate_score(visitscore.value, 501)
                    p2visit = p2.get_no_of_visits()
                    p2remscore.value = p2.get_remaining()
                    
                    if p2.get_leg_complete() != True:
                        p2.calculate_average(visitscore.value, 501, 3)
                        p2avg.value = "Overall: " + str(p2.get_average())
                        p2100s.value = "100s :" + str(p2.get_100s())
                        p2140s.value = "140s :" + str(p2.get_140s())
                        p2180s.value = "180s :" + str(p2.get_180s())
                        p1remscore.value = p1remscore.value + "*"
                        game.set_players_turn(1)
                    if p2visit < 12:#first 12 scores are placed in the left column
                        p2countdown = Text(p2scores, text=p2remscore.value, grid=[1,p2visit], size=18, align="right")
                        p2visit = Text(p2scores, text=visitscore.value, grid=[0,p2visit], size=18, align="left")
                    else:#second set of 12 scores are placed in the right column
                        p2visit = p2visit - 11
                        p2countdown = Text(p2scores, text=p2remscore.value, grid=[3,p2visit], size=18, align="right")
                        p2visit = Text(p2scores, text=visitscore.value, grid=[2,p2visit], size=18, align="left")
                        p2avg.value = "Overall: " + str(p2.get_average())
                    p2countdown.text_color = "Red"
                    
                    if p2.get_leg_complete() == True:
                        print("Player 2 Leg won")
                        p2legslbl.value = "Legs: " +str(p2.get_legs_won())
                        darts_to_finish()
                    

                visitscore.clear()

def darts_to_finish():

    finishdarts = question("Darts to finish", "How many darts to finish?", 0, app)
    if game.get_players_turn() == 1:
        p1.set_no_of_darts(finishdarts)
        p1.calculate_average(visitscore.value, 501, finishdarts)
        p1avg.value = "Overall: " + str(p1.get_average())
    else:
        print("Setting P2 darts to finish")
        p2.set_no_of_darts(finishdarts)
    
    #Set scores back to 501 and select the correct player to throw first    
    if game.get_first_throw() == 1: 
        p1remscore.value = "501"
        p2remscore.value = "501*"
        game.set_first_throw(2)
        game.set_players_turn(2)
    else:
        p1remscore.value = "501*"
        p2remscore.value = "501"
        game.set_first_throw(1)
        game.set_players_turn(1)
        
    destroyscores(p1scores, "left")
    destroyscores(p2scores, "right")    
    
    #Reset stats for the start of the next leg and set the active player to the opposite of the one who threw first in the previous leg
    p1.reset()
    p2.reset()
    visitscore.focus()
    
def destroyscores(box_name, alignment):#Destroys the scores in the players scores box!
    childstr = str(box_name.children)
    childlist = childstr.split(",")
    while len(childlist)>0:
        for child in box_name.children:
            child.destroy()
            childlist.pop()


    

app = App("Darts Calculator", width=700, height=550)

players = Box(app, align="top", width="fill") #creates a box at the top of the window that fills it horizontally
player1box = Box(players, align="left", border=1, width="fill") #creates a box inside the players box for the details of the first player
p1name = Text(player1box, text=p1.get_name(), align="top")
#p1targetscore = Text(player1box, text="501", align="bottom")

player2box = Box(players, align="right", border=1, width="fill") #creates a box inside the players box for the details of the second player
p2name = Text(player2box, text=p2.get_name(), align="top")

player1stats = Box(app, align="left", width=120, height="fill", border=1, layout="grid")#box containing all stats for player 1
player1stats.bg = "white"
p1setslbl = Text(player1stats, text="Sets: 0", grid=[0,0])#number of sets player 1 has won
p1legslbl = Text(player1stats, text="Legs: " + str(p1.get_legs_won()), grid=[0,1])
p1avglbl = Text(player1stats, text="Averages", grid=[0,4])
p1avg = Text(player1stats, text="Overall: ", grid=[0,5])
p1first3 = Text(player1stats, text="First 3: ", grid=[0,6])
p1perleg = Text(player1stats, text="Darts per leg: ", grid=[0,7])
p1tontable = Box(player1stats, width="fill", height=20, border=1, layout="grid", grid=[0,8])
p1tontabletitle = Text(p1tontable, text="Ton Table", grid=[0,9])
p1100s = Text(p1tontable, text="100s: ", grid=[0,10])
p1140s = Text(p1tontable, text="140s: ", grid=[0,11])
p1180s = Text(p1tontable, text="180s: ", grid=[0,12])


player2stats = Box(app, align="right", width=120, height="fill", border=1, layout="grid")#box containing all stats for player 2
player2stats.bg = "white"
p2setslbl = Text(player2stats, text="Sets: 0", grid=[0,0])#number of sets player 2 has won
p2legslbl = Text(player2stats, text="Legs: " + str(p2.get_legs_won()), grid=[0,1])
p2avglbl = Text(player2stats, text="Averages", grid=[0,4])
p2avg = Text(player2stats, text="Overall: ", grid=[0,5])
p2first3 = Text(player2stats, text="First 3: ", grid=[0,6])
p2perleg = Text(player2stats, text="Darts per leg: ", grid=[0,7])
p2tontable = Box(player2stats, width="fill", height=20, border=1, layout="grid", grid=[0,8])
p2tontabletitle = Text(p2tontable, text="Ton Table", grid=[0,9])
p2100s = Text(p2tontable, text="100s: ", grid=[0,10])
p2140s = Text(p2tontable, text="140s: ", grid=[0,11])
p2180s = Text(p2tontable, text="180s: ", grid=[0,12])

remainingscores = Box(app,align="top", width="fill", height=70, border=3)
remainingscores.bg = "Black"
p1remscore = Text(remainingscores, text="501", align="left", size=48)
p1remscore.text_color = "Red"
p2remscore = Text(remainingscores, text="501", align="right", size=48)
p2remscore.text_color = "Red"

scoresperturn = Box(app, align="top", width="fill", height=30, border=1)#houses the score entry field
visitscore = TextBox(scoresperturn, align="bottom", width=15)

p1scores = Box(app, align="left", width=210, height="fill", border=1, layout="grid")
p2scores = Box(app, align="right", width=210, height="fill", border=1, layout="grid")


#Add asterix to the player's score to denote whose throw it is
if game.get_players_turn() == 1:
    p1remscore.value = p1remscore.value + "*"
else:
    p2remscore.value = p2remscore.value + "*"

visitscore.focus()
visitscore.when_key_pressed = enter_pressed

app.display()
