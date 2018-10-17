num=int(input("Enter a number:"))
def absolute_value(num):
    """this function returns the absolute value of entered numebr"""

    if num>0:
        return num
    else:
        return -num

abs=absolute_value(num)
print(abs)

