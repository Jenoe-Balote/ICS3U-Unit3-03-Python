#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program is the better "Number Guessing Game"

import random
n = random.randint(0, 9)


def main():
    # this function runs the better "Number Guessing Game"

    # input
    number_guessed = int(input("Enter a number between 0 - 9: "))
    print("")

    # process and output
    if number_guessed == n:
        print("You guessed correctly!")
    else:
        print("Incorrect, the number was {}.".format(n))


if __name__ == "__main__":
    main()
