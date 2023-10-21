from Game import TruOrFalse
from GameStatus import GameStatus


game = TruOrFalse()
game.start_game()

while game.get_game_status == GameStatus.IN_PROGRES:
    print(game.next_question())
    game.get_answer()
    game.check_status()



