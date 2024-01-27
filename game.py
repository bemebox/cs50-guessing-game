import random


def get_positive_integer(text, with_zero):
    # while the user does not input a positive integer
    while True:
        try:
            # prompts the user for a positive integer
            int_number = int(input(text).strip())
            if int_number > 0:
                # if the user type a positive integer then return the value
                return int_number
            elif int_number == 0 and with_zero:
                # if the user type zero and zero is allowed
                return int_number
        except ValueError:
            # if the user does not input a positive integer, then prompt again
            pass


def main():
    # prompts the user for a level, n.
    user_level = get_positive_integer("Level: ", False)

    # randomly generates an integer between 1 and user level,
    # inclusive, using the random module.
    chosen_number = random.randint(1, user_level)

    # prompts the user to guess the integer
    gess_number = 0
    while gess_number != chosen_number:
        try:
            gess_number = get_positive_integer("Guess: ", True)
            if gess_number < chosen_number:
                # if the guess is smaller than that integer,
                # the program should output Too small! and prompt the user again.
                print("Too small!")
            elif gess_number > chosen_number:
                # if the guess is larger than that integer,
                # the program should output Too large! and prompt the user again.
                print("Too large!")
            else:
                # if the guess is the same as that integer,
                # the program should output Just right! and exit.
                print("Just right!")
                break
        except (KeyboardInterrupt, EOFError):
            # handle the command+c and command+d input to break the while loop
            break


if __name__ == "__main__":
    main()
