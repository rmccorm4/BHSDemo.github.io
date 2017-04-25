#Game to guess a number between 1-10, or any range you choose
import random

number = str(random.randint(1, 10))
guess = input("Guess a number between 1 and 10: ")

print(number)

if guess == number:
	print("You won!")

else:
	print("You lost!")
