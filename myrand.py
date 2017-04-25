import random

#this game is to guess a number between 1-10
number = str(random.randint(1, 10))
guess = input("Guess a number between 1 and 10: ")

print("The actual number was", number)

if number == guess:
	print("You got it!")

else:
	print("Better luck next time!")
