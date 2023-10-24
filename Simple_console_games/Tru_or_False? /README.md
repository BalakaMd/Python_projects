```markdown
# True or False Game

This is a simple Python-based True or False quiz game that reads questions from a CSV file
and challenges players to answer with 'yes' or 'no.' The objective is to achieve a 70%
or higher correct answer rate.

## Features

- Randomly selects questions from a CSV file.
- Allows players to input 'yes' or 'no' as answers.
- Provides an explanation for each question.
- Tracks the number of correct answers.
- Offers a win condition when 70% of questions are answered correctly.
- Ends the game if the player runs out of attempts.

## Usage

To start the game, run the `start_game` method. It will prompt you to enter
the number of questions you want to answer.
The game will keep running until you either reach the win condition or run out of attempts.
```

```python
game = TruOrFalse()
game.start_game()
```


## How to Play

- Enter 'yes' or 'no' when prompted for an answer.
- The game will inform you if your answer is correct or not and provide an explanation.
- The game will track the number of correct answers and end if you meet the win condition or run out of attempts.

## Configuration

You can change the questions file by using the `change_file_questions` method:

```python
game.change_file_questions("new_questions.csv")
```

Make sure the new file is in CSV format.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. If you have new questions to add to the game, make sure they are in the correct CSV format.

Enjoy the game!

## Authors

- BalakaMd
