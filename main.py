from game_class import *

#configure parameters
GAME_LENGTH = 20
PLAYER_AMOUNT = 5

if __name__ == '__main__':
    game = Game(GAME_LENGTH, PLAYER_AMOUNT)
    game.begin()
    while game.check_game_over() is False:
        for player in game.player_list:
            input()
            roll = player.roll_die()
            print('player {} roll {}'.format(game.game_icon[game.player_list.index(player)],roll))
            game.update_position(game.player_list.index(player))
            game.display_state()
            if game.check_game_over() is True:
                break
    game.print_results()
