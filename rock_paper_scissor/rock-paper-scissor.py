class Player:
    def __init__(self):
        self.points = 0
        self.choice = ""

class GameRound:
    pass

class Game:
    def __init__(self):
        self.endGame = False
        self.player_1 = Player()
        self.player_2 = Player()