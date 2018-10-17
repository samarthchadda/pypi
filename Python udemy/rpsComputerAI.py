import random


player=input("Player, make your move:").lower()
rand_num=random.randint(0,2); #can be from (1,3) or (8,10)

if rand_num==0:
	computer="rock"
elif rand_num==1:
	computer="paper"
else:
	computer="scissors"

print(f"computer plays {computer}")



if player == computer:
	print("It is a tie!")
elif player=="rock":
	if computer=="scissors":
		print("Player Wins!")
	else:
		print("Computer Wins!")
elif player=="paper":
	if computer=="rock":
		print("Player Wins!")
	else:
		print("Computer Wins!")
elif player=="scissors":
	if computer=="rock":
		print("Computer Wins!")
	else:
		print("Player Wins!")
else:
	print("Something went wrong")
