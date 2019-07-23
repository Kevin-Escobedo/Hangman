#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from hangman_logic import HangmanGame
import tkinter
import os
import sys

class HangmanGUI:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.geometry("300x150")
        self.root_window.title("Hangman")
        self.root_window.resizable(0, 0)
        self.enter_letter = tkinter.Entry(self.root_window, width = 5)
        self.game = HangmanGame()
        self.past_letters = tkinter.StringVar()
        self.lines = tkinter.StringVar()

    def resource_path(self, relative_path):
        '''Get absolute path to resource, works for dev and for PyInstaller'''
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def check_game_over(self):
        '''Checks if the game is over'''
        return self.game.tries != 0 and self.game.num_letter != 0

    def run(self):
        tkinter.Label(self.root_window, textvariable = self.lines).grid(row = 0, column = 0)
        tkinter.Label(self.root_window, text = "Guess a Letter: ").grid(row = 1, column = 0)

        self.enter_letter.grid(row = 1, column = 1)

        if len(self.game.guessed_letters) != 0:
                self.past_letters.set(str(self.game.guessed_letters))

        self.lines.set(self.game.show_lines)
        self.root_window.mainloop()


if __name__ == "__main__":
    HangmanGUI().run()
