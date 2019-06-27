class HangmanGame:
    def __init__(self, tries = 6):
        self.tries = tries
        self.word = self.get_word()
        self.guessed_letters = set()
        self.show_lines = self.generate_lines(self.word)
        self.num_letter = len(self.word)

    def get_word(self):
        from random import randrange
        file = open("hangman_words.txt", "r").readlines()
        return file[randrange(len(file))].upper().strip()

    def generate_lines(self, word:str):
        hidden_word = ""
        for letter in word:
            if letter.isalpha():
                hidden_word += "-"
            else:
                hidden_word += letter
        return hidden_word
        
    def get_guess(self):
        while True:
            try:
                guess = input("Guess a letter: ")
                if not guess.isalpha() or len(guess) != 1 or guess in self.guessed_letters:
                    raise ValueError
                return guess.upper()
            except ValueError:
                print()

    def check_guess(self, guess:str):
        return guess in self.word

    def update_hidden_word(self, index:int):
        hidden_word = ""
        for i in range(len(self.word)):
            if i == index:
                hidden_word += "{}".format(self.word[i])
            else:
                hidden_word += self.show_lines[i]
        return hidden_word

    def update_game(self, guess:str):
        if self.check_guess(guess):
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.num_letter -= 1
                    self.show_lines = self.update_hidden_word(i)
        else:
            self.tries -= 1
            self.guessed_letters.add(guess)
        

if __name__ == "__main__":
    game = HangmanGame()
