import guessing_game
import hangman_game


def read_int(txt):
    while True:
        try:
            option = int(input(txt))
        except (ValueError, TypeError):
            print("\033[0;31mError! Choose a integer number.\033[m")
        else:
            return option


def play():
    print("*******************")
    print("       GAMES       ")
    print("*******************")
    print("1 - Guessing Game  ")
    print("2 - Hangman Game   ")
    while True:
        game = read_int("Choose your game: ")
        if game == 1:
            guessing_game.play()
            break
        if game == 2:
            hangman_game.play()
            break
        print("\033[0;31mError! Choose a valid Game (1,2)\033[m")


if __name__ == "__main__":
    play()
