from game_class import *
import sys
#configure parameters
GAME_LENGTH = 20
PLAYER_AMOUNT = 5

if __name__ == '__main__':
    if len(sys.argv)!=1:
        if len(sys.argv)!=3:
            sys.exit('need exactly two arguments instead of. Usage python3 main.py <game length> <player amount> \nIf no game length and player amount is enter, game length is 20 and player amount is 5')
        else:
            try:
                game = Game(int(sys.argv[1]),int(sys.argv[2]))
            except ValueError:
                sys.exit('arguments must be integers')
    else:
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
