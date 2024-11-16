import random
import csv
from enum import Enum
from pathlib import Path
import re


class CsvFileReader:
    """
    Class for reading and modifying CSV file
    """

    def __init__(self, csv_file, directory="homework_11"):
        """
        Constructor for CSV file
        """
        self.csv_file = csv_file
        self.directory = directory
        base_dir = Path(__file__).resolve().parent.parent
        self.data_file = base_dir.joinpath(directory).joinpath(csv_file)
        self.data = self.get_data

    @property
    def get_data(self):
        """
        function for reading data from CSV file
        """

        with open(self.data_file) as file:
            reader = csv.reader(file)
            data = [','.join(row) for row in reader]

        return data


class Message(Enum):
    """
    Class for messages
    """

    INVALID = 'Invalid value. Try again.'
    WRONG = 'Wrong value. Try again!'
    WIN = 'You guess the word. Congratulation!'
    CORRECT = 'Correct! This letter is in the word.'
    INPUT_REQUEST = 'Enter the letter: '


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def show_start_screen(self):
        print(self.session.desc)
        print(["_" for _ in self.session.task])

    @staticmethod
    def fire_alert(message: str):
        print(message)

    def show_current_state(self):
        print(["_" if letter not in self.session.tries else letter for letter in self.session.task])


class GameSession:
    ALLOWED_CHARS = r"[a-zA-Z]"

    def __init__(self, task: str, desc: str):
        self.task = task
        self.desc = desc
        self.tries = []
        self.screen = ScreenView(self)

    @staticmethod
    def user_make_guess() -> str:
        """
        Receive input from user, normalize
        """

        return input(Message.INPUT_REQUEST.value).strip().lower()

    def win(self) -> bool:
        """
        Check if all letters are guessed
        """

        return set(self.task).issubset(self.tries)

    def guess_is_valid(self, guess: str) -> bool:
        """
        Check if input from user is valid
        """

        return len(guess) == 1 and re.match(self.ALLOWED_CHARS, guess)

    def save_guess(self, guess: str):
        """
        Save guess in tries
        """

        self.tries.append(guess)

    def main(self):
        self.screen.show_start_screen()

        while not self.win():
            guess = self.user_make_guess()
            if not self.guess_is_valid(guess):
                self.screen.fire_alert(message=Message.INVALID.value)

                continue

            self.save_guess(guess)

            if guess in self.task:
                self.screen.fire_alert(message=Message.CORRECT.value)
            else:
                self.screen.fire_alert(message=Message.WRONG.value)

            self.screen.show_current_state()

        self.screen.fire_alert(message=Message.WIN.value)


if __name__ == "__main__":
    file_words = CsvFileReader(csv_file="words.csv", directory="tasks_oop")
    random_word = random.choice(file_words.data)
    GameSession(random_word, 'You need to guess all letters in the random word.').main()
    print(random_word)
