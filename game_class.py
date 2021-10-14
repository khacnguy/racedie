import string
from player_class import *
class Game:
    def __init__(self, length, player_num):
        #length of the game
        self.length = length

        #player list
        self.player_list = []

        #create the player
        for i in range (player_num):
            self.player_list.append(Player(length))

        #initial game state
        self.game_state = ['O']+['-']*(length-1)

        #game icon for use
        self.game_icon = ['X','O'] + list(string.ascii_uppercase)

    def begin(self):
        print('Game begins')
        self.display_state()

    def display_state(self):
        #display the state of the game
        print('*' * self.length*3)
        print('  '.join(self.game_state))
        print('*' * self.length*3)

    def update_position(self, player_idx):
        #update the position of players

        #update the position of the player moving
        self.player_list[player_idx].update_position_player()

        #check if there is anyone in the same block
        tmp = [self.player_list[player_idx].pos == player.pos if (
                player.pos != 1 and self.player_list.index(player) != player_idx) else False for player in
               self.player_list]

        #while there are people on the same block
        if any(tmp):
            self.player_list[tmp.index(True)].pos = 1
            #recreate the tmp list

        self.game_state = ['-'] * self.length

        #update game state
        for player in self.player_list:
            self.game_state[player.pos-1] = self.game_icon[self.player_list.index(player)]


    def check_game_over(self):
        for player in self.player_list:
            #check all players, if there is one on the final block return True and stop the game
            if player.pos == self.length:
                return True
        return False

    def print_results(self):
        #print out the winner of the game
        for player in self.player_list:
            if player.pos == self.length:
                print('{} is the winner'.format(self.game_icon[self.player_list.index(player)]))
