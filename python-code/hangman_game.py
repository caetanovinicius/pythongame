def menu():
    print("********************")
    print("    HANGMAN GAME    ")
    print("     F R U T S      ")
    print("********************")


def import_words():
    try:
        file = open("words.txt", "r")
    except:
        print("Error or open file")
    else:
        from random import randrange

        words = [line.replace("\n", "") for line in file]
        random_number = randrange(0, (len(words) - 1))
        return words[random_number]


def draw_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def game_over(secret_word):
    print("\033[0;31mGAME OVER!\033[m")
    print("The secret word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")


def you_win():
    print("\033[0;32mYOU WIN!\033[m")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def play():
    menu()
    secret_word = import_words()
    list_word = ["_" for i in range(len(secret_word))]
    print(list_word)
    error = 0
    while error < 7:
        your_letter = str(input("Type a letter: ")).lower().strip()
        if your_letter in secret_word:
            for index, letter in enumerate(secret_word):
                if letter == your_letter:
                    list_word[index] = letter
        else:
            error += 1
            draw_hangman(error)
        print(list_word)
        if "_" not in list_word:
            you_win()
            break
        if error == 7:
            game_over(secret_word)


if __name__ == "__main__":
    play()
