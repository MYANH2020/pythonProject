import random
roll = random.randint(1,6)
guess = int(input('guess the dice roll:\n'))
if guess == roll:
    print(" Correct! They rolled a " + str(roll))
else:
    print(" wrong! They rolled a "+ str(roll))