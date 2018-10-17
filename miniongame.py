s=input()
vowels='AEIOU'
kevsc=0
stusc=0
for i in range(len(s)):      #i is iterator for length of substring
    if s[i] in vowels:
        kevsc+=(len(s)-i)
    else:
        stusc+=(len(s)-i)
    
if kevsc>stusc:
    print("Kevin",kevsc)
elif stusc>kevsc:
    print("Stuart",stusc)
else:
    print("Draw")
