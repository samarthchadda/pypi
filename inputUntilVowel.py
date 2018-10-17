vowels='aeiouAEIOU'

#infinite loop
while True:
    v=input('Enter a vowel:')

    if v in vowels:
        break
    print('This is not a vowel. Try again!')


print("Thank you!")
