class Game_info():
    def __init__(self):
        self.throwing_first = 1
        self.players_turn = 1
        
    def set_first_throw(self, player):
        self.throwing_first = player
        
    def get_first_throw(self):
        return self.throwing_first
    
    def set_players_turn(self, player):
        self.players_turn = player
        
    def get_players_turn(self):
        return self.players_turn