print("Rock....")
print("Paper....")
print("Scissors....")

pl1=input("Player 1, make your move:")
print("***NO CHEATING***\n\n"*20)
pl2=input("Player 2, make your move:")

if pl1 == pl2:
	print("It is a tie!")
elif pl1=="rock":
	if pl2=="scissors":
		print("Player 1 Wins!")
	if pl2=="paper":
		print("Player 2 Wins!")
elif pl1=="paper":
	if pl2=="rock":
		print("Player 1 Wins!")
	if pl2=="scissors":
		print("Player 2 Wins!")
elif pl1=="scissors":
	if pl2=="rock":
		print("Player 2 Wins!")
	if pl2=="paper":
		print("Player 1 Wins!")
else:
	print("Something went wrong")
