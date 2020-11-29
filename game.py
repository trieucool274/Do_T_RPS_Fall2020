#import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint 

# re-import our game variables
from gameComponents import gameVars, winLose ,rules

# define a win or lose function


# True and False are Boolean data types -> they are the equivalent of on or offf, 1 or 0 

while gameVars.player is False: 
	print("==============*/ RPS GAME /*===============")
	print("Computer Lives:",gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("=========================================")
	print("Choose your weapon! or type quit to exit \n")
	gameVars.player = input("Choose rock, paper or scissors: \n")

	#if the gameVars.player chose to quit, then exit the game 
	if gameVars.player =="quit":
		print("you chose to quit,quitter!")
		exit()

	#gameVars.player = True -> it has value (rock, paper, or scissors)


	# this will be the gameVars.computer choice -> a random pick from the choices array
	computer = gameVars.choices[randint(0, 2)]

	# check to see what the user input

	# print outputs whatever is in the round brackets -> in this case it outputs gameVars.player to the command prompt window
	print("user chose: " + gameVars.player)

	#validate that   the random choice worked for the gameVars.computer
	print("AI chose: " + computer)

	rules.rules()

	
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

		
	elif  gameVars.computer_lives == 0:
		winLose.winorlose("won")
	
	else:
		gameVars.player = False

		
		# print("Winner! Would you like to play aggameVars.computern?")
		# choice = input("Y / N? ")

		# if choice == "N" or choice == "n": 
		#	print("You chose to quit! Better luck next time!")
		#	exit()

		#elif choice =="Y" or choice =="y":
			# reset the gameVars.player lives and the gameVars.computer lives
			# and set gameVars.player to False so that our loop will restart
		#	gameVars.player_lives = 1
		#	gameVars.computer_lives = 1
		#	gameVars.player = False
		
		#else:
		#	print("Make a valid choice - Y or N")
			# this will generate a bug that we need to fix later
		#	choice = input("Y / N")		


	#print("gameVars.player has ", gameVars.player_lives, "lives left")
	#print("gameVars.computer lives:", gameVars.computer_lives, "lives left")

	# make the loop keep running by setting gameVars.player back to False
	#unset, so that our loop condition above will evaluate to True
	#gameVars.player = False 









