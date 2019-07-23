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
        self.enter_letter = tkinter.Entry(self.root_window, width = 6)
        self.game = HangmanGame()
        self.past_letters = tkinter.StringVar()
        self.lines = tkinter.StringVar()
        self.error_message = tkinter.StringVar()
        self.tries = tkinter.StringVar()

    def resource_path(self, relative_path):
        '''Get absolute path to resource, works for dev and for PyInstaller'''
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def check_not_game_over(self):
        '''Checks if the game is over'''
        return self.game.tries > 0 and self.game.num_letter != 0

    def get_the_guess(self):
        '''Gets the guess from the Entry box'''
        try:
            guess = self.enter_letter.get()
            if not guess.isalpha():
                raise TypeError
            if len(guess) != 1:
                raise ValueError
            if guess in self.game.guessed_letters:
                raise IndexError
            self.enter_letter.delete(0, tkinter.END)
            return guess.upper()
        except TypeError:
            self.error_message.set("ERROR: Entry not a letter")
        except ValueError:
            self.error_message.set("ERROR: Entry must be single letter")
        except IndexError:
            self.error_message.set("ERROR: Entry already guessed")
                


    def check_guess(self):
        '''Checks if the guessed letter is in the word'''
        if self.check_not_game_over():
            guess = self.get_the_guess()
            try:
                self.game.update_game(guess)
                self.error_message.set("")
            except TypeError:
                pass
            if len(self.game.guessed_letters) > 0:
                self.past_letters.set(str(self.game.guessed_letters))
            self.lines.set(self.game.show_lines)
            self.tries.set("Tries Left: {}".format(self.game.tries))
            if self.game.tries == 0:
                self.lines.set(self.game.word)
                self.tries.set("Game Over")
        else:
            self.lines.set(self.game.word)
            self.tries.set("Game Over")

    def key(self, event):
        '''Handles keyboard input'''
        if event.keysym == "Return":
            self.check_guess()

    def run(self):
        tkinter.Label(self.root_window, textvariable = self.lines).pack()
        self.enter_letter.pack()

        guess_button = tkinter.Button(self.root_window, text = "Guess",  command = self.check_guess)
        guess_button.pack()

        tkinter.Label(self.root_window, textvariable = self.past_letters).pack()
        tkinter.Label(self.root_window, textvariable = self.tries).pack()

        tkinter.Label(self.root_window, textvariable = self.error_message).pack()


        if len(self.game.guessed_letters) > 0:
            self.past_letters.set(str(self.game.guessed_letters))

        self.lines.set(self.game.show_lines)


        self.root_window.bind("<KeyPress>", self.key)

        self.tries.set("Tries Left: {}".format(self.game.tries))

        self.root_window.mainloop()


if __name__ == "__main__":
    HangmanGUI().run()
