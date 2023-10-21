total_sticks = 10
print("Hi and let's try to play old Chinese Stick Game!\n"
      "It's a game for two players. There are 10 sticks on a table.\n"
      "Each player takes turns taking one, two or three sticks from the table.\n"
      "The one who takes the last stick from the table loses\n"
      "Let's try and Good luck !\n"
      "")
player1 = input("Enter First Player name: ")
player2 = input("Enter Second Player name: ")

while total_sticks != 0:
    turn_player1 = []
    turn_player2 = []
    # Turn player 1
    try:
        turn_player1 = int(input(f"{player1} Your turn: "))
    except ValueError:
        print("You need enter only numbers between 1 - 3")
    if turn_player1 not in [1, 2, 3]:
        print("You can take only 1, 2 or 3 sticks")
        continue
    else:
        total_sticks = total_sticks - turn_player1
        if total_sticks <= 0:
            print(f"{player1} You blow! {player2} Wins !")
            break
    print(f"The are {total_sticks} sticks on a table")

    # Turn player 2
    try:
        turn_player2 = int(input(f"{player2} Your turn: "))
    except ValueError:
        print("You need enter only numbers between 1 - 3")
    while turn_player2 not in [1, 2, 3]:
        print("You can take only 1, 2 or 3 sticks")
        try:
            turn_player2 = int(input(f"{player2} Your turn: "))
        except ValueError:
            print("You need enter only numbers between 1 - 3")
    else:
        total_sticks = total_sticks - turn_player2
        if total_sticks <= 0:
            print(f"{player2} You blow! {player1} Wins !")
            break
        print(f"The are {total_sticks} sticks on a table")
