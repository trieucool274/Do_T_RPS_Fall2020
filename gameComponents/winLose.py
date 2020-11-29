from gameComponents import gameVars 

def winorlose(status):
	# print("inside winorlose function; status is: ", status)

	if status == "won":
		pre_message = "You are the winner! "
	else:
		pre_message = "you are lose!"

	print(pre_message + "! Would you like to play again?")

	choice = input("Y / N? ")

	if choice =="Y" or choice =="y":
		# reset the player lives and the gameVars.computer lives
		# and set player to False so that our loop will restart

		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.player = False 
	
	elif choice == "N" or choice == "n":
		# exit message and quit
		print("You chose to quit. Better luck next time!")
		exit ()
	
	else:
		print("Make a valid choice - Y or N")
		# this will generate a bug that we need to fix later
		choice = input("Y / N")
