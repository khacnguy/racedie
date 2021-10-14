import random
class Player:
    def __init__(self,length):
        #initial position is 1
        self.pos = 1

        #store the rolling history
        self.die_rolled = []

        #the length of the game
        self.length = length

    def roll_die(self):
        #roll the dice
        die = random.randint(1,6)
        self.die_rolled.append(die)
        return die

    def update_position_player(self):
        #update the player position
        #check if it is out of the length of the game
        if self.pos + self.die_rolled[-1]  <= self.length:
            self.pos += self.die_rolled[-1]
