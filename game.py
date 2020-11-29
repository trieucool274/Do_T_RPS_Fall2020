#import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint 

# [] => this is an array. an array is a speacial type of container that can hld multiple items 
# array are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]



player_lives = 1
ai_lives = 1

total_lives = 1 

# define a win or lose function
def winorlose(status):
	# print("inside winorlose function; status is: ", status)

	if status =="won":
		pre_message = "You are the winner! "
	else:
		pre_message = "you are lose! "

	print("You", status, "! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n": 
		print("You chose to quit! Better luck next time!")
		exit()

	elif choice =="Y" or choice =="y":
		# reset the player lives and the AI lives
		# and set player to False so that our loop will restart
		global player_lives 
		global ai_lives
		global player

		player_lives = 1
		ai_lives = 1
		player = False
	
	else:
		print("Make a valid choice - Y or N")
		# this will generate a bug that we need to fix later
		choice = input("Y / N")


 # True and False are Boolean data types -> they are the equivalent of on or offf, 1 or 0 
player = False 

while player is False: 
	print("==============*/ RPS GAME /*===============")
	print("Computer Lives:",ai_lives, "/", total_lives)
	print("Player Lives:", player_lives, "/", total_lives)
	print("=========================================")

	print("Choose your weapon! or type quit to exit\n")
	#this is the player choice
	player = input("Choose rock, paper or scissors: \n")

	#if the player chose to quit, then exit the game 
	if player =="quit":
		print("you chose to quit")
		exit()

	#player = True -> it has value (rock, paper, or scissors)


	# this will be the AI choice -> a random pick from the choices array
	computer = choices[randint(0, 2)]

	# check to see what the user input

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + player)

	#validate that   the random choice worked for the AI
	print("AI chose: " + computer)

	if (computer == player):
		print("tie")

	elif (computer == "rock"):
		if (player == "scissors"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1

	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1
	if player_lives is 0:
		winorlose("lost")

		
	if ai_lives is 0:
		winorlose("won")
		
		# print("Winner! Would you like to play again?")
		# choice = input("Y / N? ")

		# if choice == "N" or choice == "n": 
		#	print("You chose to quit! Better luck next time!")
		#	exit()

		#elif choice =="Y" or choice =="y":
			# reset the player lives and the AI lives
			# and set player to False so that our loop will restart
		#	player_lives = 1
		#	ai_lives = 1
		#	player = False
		
		#else:
		#	print("Make a valid choice - Y or N")
			# this will generate a bug that we need to fix later
		#	choice = input("Y / N")		


	print("player has ", player_lives, "lives left")
	print("ai lives:", ai_lives, "lives left")

	# make the loop keep running by setting player back to False
	#unset, so that our loop condition above will evaluate to True
	player = False 









