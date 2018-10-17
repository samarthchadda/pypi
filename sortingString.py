text=input("Enter a string:")

#breakdown the string into list of words
words=text.split()

#sort the list
words.sort()

#display the sorted words
print("Sorted words are:")
for word in words:
    print(word)
