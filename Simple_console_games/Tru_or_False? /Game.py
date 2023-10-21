import csv
import random
from GameStatus import GameStatus


class TruOrFalse:
    file = "Questions.csv"
    read_file = csv.reader(open(file))
    new_list = [line for line in read_file]
    question = []
    answer = []
    explanation = []
    counter = 0

    def __init__(self, number_of_attempts=2):
        self.__number_of_attempts = number_of_attempts
        self.__game_status = GameStatus.NOT_STARTED
        self.question = self.question
        self.answer = self.answer
        self.explanation = self.explanation
        self.win_percent = ...
        self.question_counter = 0

    @classmethod
    def change_file_questions(cls, new_file: str):
        """
        Accepts a new file path in the format 'str'.
        A new file need be in format .csv.
        """
        cls.file = new_file

    def next_question(self):
        self.question_counter += 1
        print(f"Question number {self.question_counter}:")
        line = random.choice(self.new_list)
        question, answer, explanation = line[0].split(';')
        self.question = question
        self.answer = answer.lower()
        self.explanation = explanation
        return question

    def get_answer(self):
        chk = True
        while chk:
            user_answer = input("PLease give answer Y/N: ").lower()
            if user_answer not in ['y', 'n', 'yes', 'no']:
                print("Please enter only yes or no ")
                continue
            else:
                chk = False
                print("")
                if user_answer in ['y', 'yes']:
                    user_answer = "yes"
                else:
                    user_answer = 'no'
            if user_answer == self.answer.strip():
                self.counter += 1
                print("Cool! Very nice")
                print(self.explanation)
                print(f"Вам осталось набрать {self.win_percent - self.counter} балл/ов")
                print("")
            else:
                print("No, its not true")
                print(self.explanation)
                print("")
                self.__number_of_attempts -= 1
                print(f"у вас осталось {self.__number_of_attempts} попыток")

    @property
    def get_game_status(self):
        return self.__game_status

    def start_game(self):
        print("Hi! Welcome to the True or False video game!\n"
              "You need to answer 'yes' or 'no' questions and get 70% correct answers.Good luck !")
        while True:
            try:
                new_number_of_attempts = int(input("PLease enter number of questions: "))
                break
            except ValueError:
                print("Please enter only numbers")
        self.__number_of_attempts = new_number_of_attempts
        self.win_percent = int(self.__number_of_attempts * 0.7)
        self.__game_status = GameStatus.IN_PROGRES

    def check_status(self):
        if self.__number_of_attempts == 0:
            self.__game_status = GameStatus.LOST
            print("Sorry you blow !")

        if self.counter == self.win_percent:
            self.__game_status = GameStatus.WON
            print("Excellent! You won!")




