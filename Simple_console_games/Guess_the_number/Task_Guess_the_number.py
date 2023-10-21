import random

number = random.randint(1, 50)
count = 1
check = True
print("Hi and welcome to the 'Guess the number video game'!\n"
      "Try to guess the number between 1 and 50.\n"
      "You have 6 attempts.\n"
      "Good luck !")

while count < 7:
    user_input = input(f"Enter the number ({count} attempt) ")
    try:
        int(user_input)
    except ValueError:
        print("Enter only numbers")
        continue
    user_input = int(user_input)
    count += 1
    if user_input != number and count == 7:
        print(f"Sorry but didn't take it:( A number was {number}")
        break
    if user_input > number:
        print("Your number is higher. Pls try again")
    elif user_input < number:
        print("Your number is lower. Pls try again")
    else:
        print(f"Yes, it's right! Number is {number}\n"
              "Congratulations!")
        break
