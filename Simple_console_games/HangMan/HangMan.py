import random


class HangMan:
    def __init__(self, errors=10):
        self.errors = errors
        self.game_world = ""
        self.game_stage = ""
        self.used_laters = []

    with open(file="WordsStockRus.txt") as WS:
        wordsStockRus = [line for line in WS]

    def word_generation(self):
        self.game_world = random.choice(self.wordsStockRus)
        self.game_stage = '_' * (len(self.game_world) - 1)
        print(f'В слове {len(self.game_world) - 1} букв')

    def player_turn(self, latter):
        self.used_laters.append(latter)
        if latter.lower() in self.game_world:
            indexes = [i for i, j in enumerate(self.game_world) if j == latter]
            for i in indexes:
                self.game_stage = self.game_stage[:i] + latter + self.game_stage[i+1:]
            else:
                print(f"Cool!\nThis is your part of word {self.game_stage}")
        else:
            self.errors = (self.errors - 1)
            print("Sorry, the word doesn't have this letter")

    def get_errors(self):
        return self.errors


alphabet = ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х',
            'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э',
            'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ё', 'ъ', 'я']

print("Hi and welcome to the HangMan!\n"
      "You need to guess the word in a certain number of attempts\n"
      "Always enter only one russian letter\n"
      "If you want to see the letters that you have already tried, write 'List'\n"
      "For quit print 'Q' \n"
      "Good luck!\n")  # Game rules

chk = True
numbers_of_errors = 10
while chk:
    try:
        numbers_of_errors = int(input("Enter how many tries you want: "))
        chk = False
    except ValueError:
        print("Enter numbers only")

start = HangMan(numbers_of_errors)
start.word_generation()


while start.errors > 0:
    player_turn = input("Please, enter the letter: ")
    print("")
    if player_turn.lower() == "q":
        print("Thank you and goodbye!:)")
        break
    if player_turn.lower() in start.used_laters:
        print('Вы уже вводили эту букву')
        continue
    if player_turn.lower() == "list":
        print(f"You used these letters {sorted(set(start.used_laters))}")
    if player_turn.lower() not in alphabet or len(player_turn) > 1:
        print("Enter only one russian letter")
        continue
    start.player_turn(player_turn)
    print(f"You have {start.get_errors()} tries\n")
    if start.errors == 0:
        print(f"Sorry, you lose. The word was '{start.game_world}'\n"
              f"Good luck next time!")
    if start.game_world == start.game_stage + "\n":
        print("Congratulations! You win!!!")
        print(f"The word was '{str(start.game_world)}'")
        break
