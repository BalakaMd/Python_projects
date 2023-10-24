# Hangman Game

## Introduction
This repository contains a simple implementation of the classic Hangman word-guessing game in Python. In this game, you are tasked with guessing a random word, letter by letter, before you run out of allowed errors.

## Game Rules
- You have a limited number of attempts to guess the word. By default, there are 10 attempts, but you can set the number of attempts when starting the game.
- You need to guess a Russian word by entering one letter at a time.
- If you want to view the letters you've already guessed, type 'List'.
- To quit the game, type 'Q'.
- You win the game if you successfully guess the entire word.
- You lose the game if you run out of attempts before guessing the word.

## Getting Started
1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Run the game by executing the script using a Python interpreter.

```python
python HangMan.py
```

4. Follow the on-screen instructions to play the game.

## How to Play
1. You will be prompted to enter the number of attempts you want before starting the game.
2. A random Russian word will be selected for you to guess. The word's length will be indicated with underscores.
3. Guess one letter at a time by typing it and pressing Enter.
4. You will be informed if the letter is correct and where it appears in the word.
5. The game will continue until you win or run out of attempts.

## Game Sample
Here's an example of how the game will be played:
```
Hi and welcome to the Hangman!
You need to guess the word in a certain number of attempts
Always enter only one Russian letter
If you want to see the letters that you have already tried, write 'List'
To quit, type 'Q'
Good luck!

Enter how many tries you want: 10
В слове 6 букв

Please, enter the letter: о

Cool!
This is your part of the word: ______о
You have 10 tries

Please, enter the letter: л

Cool!
This is your part of the word: __л___о
You have 10 tries

Please, enter the letter: а

Cool!
This is your part of the word: ал___о
You have 10 tries

Please, enter the letter: р

Cool!
This is your part of the word: алр__о
You have 10 tries

Please, enter the letter: т

Cool!
This is your part of the word: алрто
You have 10 tries

Congratulations! You win!!!
The word was 'алрто'
```

## Author
* BalakaMD

If you have any questions or suggestions, please feel free to reach out.

Have fun playing the game!
