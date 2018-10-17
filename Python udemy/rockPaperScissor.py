print("Rock....")
print("Paper....")
print("Scissors....")

pl1=input("Player 1, make your move:")
pl2=input("Player 2, make your move:")


if pl1=="rock" and pl2=="scissors":
    print("Player 1 Wins!")
elif pl1=="rock" and pl2=="paper":
	print("Player 2 Wins!")
elif pl1 =="paper" and pl2=="rock":
	print("Player 1 Wins!")
elif pl1=="paper" and pl2=="scissors":
	print("Player 2 Wins!")
elif pl1=="scissors" and pl2=="rock":
	print("Player 2 Wins!")
elif pl1=="scissors" and pl2=="paper":
	print("Player 1 Wins!")
elif pl1==pl2:
	print("It is a tie!")
else:
	print("Something went wrong")
