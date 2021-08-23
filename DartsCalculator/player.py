from tkinter import messagebox
class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.average = 0
        self.darts = 0
        self.remaining = 501
        self.scores = []
        self.visits = 0
        self.legswon = 0
        self.legcomplete = False
        self.hundreds = 0
        self.hundredforties = 0
        self.hundredeighties = 0
        self.first3 = []
        self.bust = False

    def set_name(self, player_name):
        self.name = player_nam

    def get_name(self):
        return self.name

    def get_average(self):
        return self.average

    def get_remaining(self):
        return self.remaining

    def get_no_of_darts(self):
        return self.darts
        print(self.darts)

    def set_no_of_darts(self, no_of_darts):
        self.darts = self.darts + int(no_of_darts)

    """Returns the number of visits the player has had to the board"""
    def get_no_of_visits(self):
        return self.visits
        print(self.visits)

    def get_legs_won(self):
        return self.legswon

    def get_leg_complete(self):
        return self.legcomplete

    def get_100s(self):
        return self.hundreds

    def get_140s(self):
        return self.hundredforties

    def get_180s(self):
        return self.hundredeighties

    def get_first3(self):
        return self.first3

    def set_first3(self, firstscore):
        self.first3.append(firstscore)
        
    def get_bust(self):
        return self.bust

    def reset(self):
        self.remaining = 501
        self.darts = 0
        self.visits = 0
        self.legcomplete = False

    def calculate_average(self, score, targetscore, no_darts):
        scorecheck = int(self.remaining) - int(score)
        self.average = (targetscore - self.remaining)/self.darts*int(no_darts)
        self.average = round(self.average, 2)

    def calculate_score(self, score, targetscore):
            scorecheck = int(self.remaining) - int(score)
            if scorecheck > 0:
                self.scores.append(score)
                self.remaining = self.remaining - int(score)
                self.darts = int(self.darts) + 3
                self.visits = self.visits+1
                if int(score) >99 and int(score) <140:
                    self.hundreds = self.hundreds + 1
                elif int(score) >139 and int(score) <179:
                    self.hundredforties = self.hundredforties+ 1
                elif int(score) == 180:
                    self.hundredeighties = self.hundredeighties+ 1

            #score has been busted
            elif scorecheck < 0:
                print("Bust score")
                self.bust = True

            #leg has finished
            elif scorecheck == 0:
                self.legswon = self.legswon + 1
                self.legcomplete = True

