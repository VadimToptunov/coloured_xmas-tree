#! /usr/bin/python

import random
import sys
from termcolor import colored

def xmas_tree():
    crown = random.randint(10, 45)
    trunk_hight = [1, 2, 3]
    trunk = random.choice(trunk_hight)
    for i in range(crown):
        for a in range(crown-i):
            sys.stdout.write(" ")
        sys.stdout.write(colored("/", "green"))
        for l in range(i<<1):
            if i==crown-1:
                sys.stdout.write(colored("~", "green"))
            else:
                list_symbs = ["@", "#", "$", "*", "+", "-", "x", "_", " "]
                list_colors = ["red", "green", "blue", "yellow"]
                symbol = random.choice(list_symbs)
                color = random.choice(list_colors)
                sys.stdout.write(colored(symbol, color))
        sys.stdout.write(colored("\\", "green"))
        print("")
    for o in range(trunk):
        for i in range(crown):
            sys.stdout.write(" ")
        print("| |")

if __name__ == "__main__":
    xmas_tree()
