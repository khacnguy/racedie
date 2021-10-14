from game_class import *

#configure parameters
GAME_LENGTH = 10
PLAYER_AMOUNT = 3

game = Game(GAME_LENGTH,PLAYER_AMOUNT)
if __name__ == '__main__':
    print('Game begins')
    game.display_state()
    while game.check_game_over() is False:
        for player in game.player_list:
            input()
            roll = player.roll_die()
            print('player {} roll {}'.format(game.game_icon[game.player_list.index(player)],roll))
            game.update_position(game.player_list.index(player))
            game.display_state()
            if game.check_game_over() is True:
                print('a')
                break
    game.print_results()
