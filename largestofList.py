def max_in_list(lst):
    max=lst[0]
    for a in lst:
        if a>max:
            max=a
    return max

x=[1,2,10,18,3]
print(max_in_list(x))

