from hangman_logic import HangmanGame

if __name__ == "__main__":
    game = HangmanGame()
    while game.tries != 0 and game.num_letter != 0:
        if len(game.guessed_letters) != 0:
            print(game.guessed_letters)
        print(game.show_lines)
        guess = game.get_guess()
        game.update_game(guess)
    print("Word: {}".format(game.word))
