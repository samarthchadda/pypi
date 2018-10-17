age=input("How old are you: ")
if age:
    age=int(age)  #casting
    if age >=18 and age<21:
        print("You can enter, but need a wristband!")
    elif age >=21:
        print("You are good to enter and can drink")
    else:
        print("you can't come as are too young")
else:
    print("Please enter a age")
    
