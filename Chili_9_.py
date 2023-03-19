from random import randint
from sys import exit
#you could do 'import random' but then ud need to write x = random.randint(0, 100)
x = randint(1, 9)
prompt = 10
while int(prompt) != x:
    prompt = str(input("Guess between 0 and 10!: "))
    if(prompt.lower() == "exit"):
        exit()
    if (int(prompt) < x):
        print("Too low!")
    elif (int(prompt) > x):
        print("Too high!")
    elif (int(prompt) == x):
        print("you got it!")