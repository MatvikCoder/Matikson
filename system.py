import sys
import os
import time
import random
print('Commands in /bin, write "ls /bin" to look commands')
time.sleep(5)
os.system('clear')
time.sleep(3)

while True:
    comm = input('Enter Command>>>')
    if comm == "ls /bin":
        print("calc - Start calculator")
        print("poweroff - Power off system")
        print("random - Random number from 0 to 10")
        print("math - Game for math education")
        print("clr - Clear screen")

    if comm == "calc":
        print('Example: YOU: 2+2, MACHINE:4')
        print(eval(input("Enter>>> ")))

    if comm == "poweroff":
        print("The system will power off now!")
        time.sleep(3)
        sys.exit()

    if comm == "random":
        number = random.randint(0, 10)
        print(number)

    if comm == "math":
        a = input("5*8? ")
        if a == "40":
            print("Good!")
        else:
            print("Bad!")
        b = input("15*2? ")
        if b == "30":
            print("Good! You beat the game!")
        else:
            print("Bad! You doesn't beat the game!")

        if comm == "clr":
            os.system('clear')

