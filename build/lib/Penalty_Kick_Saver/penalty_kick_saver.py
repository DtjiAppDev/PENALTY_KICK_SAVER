"""
This file contains Python code for the game where the player needs to save a penalty kick.
Author: DtjiAppDev
"""


import random
import sys
sys.setrecursionlimit(5000)


def main():
    """
    This function is used to run the game.
    :return: None
    """

    print("In this game, the player becomes a goalkeeper whose job is to save opponent's penalty kick.")
    possible_directions: list = ["LEFT", "RIGHT", "CENTER"]
    print("Your opponent takes a penalty kick.")
    goalkeeper_direction: str = input("Please enter LEFT, RIGHT, or CENTER! ")
    while goalkeeper_direction not in possible_directions:
        goalkeeper_direction = input("Sorry, invalid input! Please enter LEFT, RIGHT, or CENTER! ")

    shot_direction: str = possible_directions[random.randint(0, len(possible_directions) - 1)]
    if shot_direction == goalkeeper_direction:
        print("You saved the shot!")
    else:
        print("Your opponent scored a goal! He kicked to the " + str(shot_direction) + "!")

    print("Enter Y for yes.")
    print("Enter anything else for no.")
    go_again: str = input("Do you want to play again? ")
    if go_again == "Y":
        main()
    sys.exit()


if __name__ == '__main__':
    main()
