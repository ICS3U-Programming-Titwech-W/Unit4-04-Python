#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: April.27. 2022

# program that generates a random correct guess. It then
# uses a loop to keep asking the user to guess
# the number until they guess correctly.
# Once they guess the correct number, it breaks out of the loop.

from colorama import Fore
import random


def main():
    # initialize the counter
    counter = 0

    # a number between 1 and 100
    random_variable = random.randint(0, 5)

    while True:
        # get the user number as a string
        user_number_string = input(Fore.WHITE + "Guess the random number between 0-5: ")
        print("")

        try:
            # convert to string
            user_number = int(user_number_string)

            # if number input is positive
            if user_number >= 0 and user_number <= 5:
                # calculate the sum of all numbers from 0 to num input
                for counter in range(1):

                    # Increment counter
                    counter = counter + 1
                if user_number == random_variable:
                    # Display result to user
                    print("")
                    print(Fore.BLUE + "{} is correct, good job!"
                          .format(user_number))
                    break
                else:
                        print(Fore.RED + "You guessed wrong, try again")
                        print("")

            else:
                print(Fore.RED + "enter a number within the range")
                print("")

        except Exception:
            print("{} is not a valid number.". format(user_number_string))


if __name__ == "__main__":
    main()
