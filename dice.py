import random
while True:
    input("Press enter to roll the dice")
    num=random.randint(1,6)
    print("You got",num)
    option=input("Roll Again(y/n)")

    #condition
    if option=='n':
        break
 
