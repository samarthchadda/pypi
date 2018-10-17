my_str=input("Enter a string:")

#caseless comparison(ignores cases when comparing)
my_str=my_str.casefold()

#reverse the string
rev_str=reversed(my_str)

#check if string is equal to its reverse
if list(my_str)==list(rev_str):
    print("It is a pailndrome")
else:
    print("It is not a palindrome")
