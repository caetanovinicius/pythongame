def menu():
    print("*******************")
    print("   GUESSING GAME   ")
    print("*******************")
    print("Guess a number between 1 and 100")


def read_int(txt):
    while True:
        try:
            number = int(input(txt))
        except (TypeError, ValueError):
            print("\033[0;31mError! Type a integer number.\033[m")
        else:
            return number


def level():
    print("1 - Easy   (15 tentatives)")
    print("2 - Medium (10 tentatives)")
    print("3 - Hard   (5 tentatives)")
    while True:
        number = read_int("Choose your game option: ")
        if 1 <= number <= 3:
            if number == 1:
                return 15
            if number == 2:
                return 10
            if number == 3:
                return 5
        print("\033[0;31mError!Type a number valid level (1,2,3)\033[m")


def play():
    menu()
    attempt = level()
    attempt_counter = attempt
    counter = 1

    from random import randint

    secret_number = randint(0, 100)

    while attempt_counter > 0:
        print(f"{counter}º from {attempt} tentatives")
        while True:
            number = read_int("Type a number: ")
            if 0 <= number <= 100:
                break
            print("\033[0;31mError!Type a number between 0 and 100\033[m")
        if number == secret_number:
            print("\033[0;32mYOU WIN!!!!")
            print("Secret Number: ", secret_number)
            print("Your Number: ", number, "\033[m")
            break
        print("To low" if secret_number > number else "To high")
        attempt_counter -= 1
        counter += 1
        if attempt_counter == 0:
            print("\033[0;31mYOU LOSE!!!!")
            print("Secret Number: ", secret_number)
            print("Your Number: ", number, "\033[m")


if __name__ == "__main__":
    play()
