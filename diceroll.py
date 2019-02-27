import random

while True:


    diceroll = random.randint(1, 10)
    guess = input("I'm thinking of a number between 1 and 10, can you guess what it is?")
    guessint = int(guess)
    if guessint == diceroll:

        print("YOU WIN!!! " + str(diceroll) +" IS the number I was thinking of!\n")
        input("Would you like to play again?")
    else:
        input("Sorry, that was NOT my number. \n Try again?")


