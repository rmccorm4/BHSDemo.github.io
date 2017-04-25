import random

ui = 'y'
while ui == 'y':
		#choice will be 0, 1, or 2
		choice = random.randint(1, 100) % 3

		opp = ""
		if choice == 1:
			opp = "Rock"
		elif choice == 2:
			opp = "Paper"
		else:
			opp = "Scissors"

		you = input("Enter Rock, Paper, or Scissors: ")
		while((you.lower() != "rock") and (you.lower() != "paper") and (you.lower() != "scissors")):
			print("You didn't enter rock, paper, or scissors! That's messed up...")
			you = input("Enter Rock, Paper, or Scissors: ")

		print("You played:", you)
		print("Opponent played:", opp)

		if(you.lower() == "rock" and opp.lower() == "scissors"):
			print("You win!")	
		elif(you.lower() == "rock" and opp.lower() == "paper"):
			print("You lose!")
		elif(you.lower() == "rock" and opp.lower() == "rock"):
			print("You tied!")
		elif(you.lower() == "paper" and opp.lower() == "rock"):
			print("You win!")
		elif(you.lower() == "paper" and opp.lower() == "scissors"):
			print("You lose!")
		elif(you.lower() == "paper" and opp.lower() == "paper"):
			print("You tied!")
		elif(you.lower() == "scissors" and opp.lower() == "paper"):
			print("You win!")
		elif(you.lower() == "scissors" and opp.lower() == "rock"):
			print("You lose!")
		elif(you.lower() == "scissors" and opp.lower() == "scissors"):
			print("You tied!")
		else:
			print("something weird happened?")

		ui = input("Press 'y' to play again or anything else to quit: ")
