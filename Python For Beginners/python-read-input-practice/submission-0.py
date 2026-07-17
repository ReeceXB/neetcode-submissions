def add_two_numbers() -> int:
    newlist = input().split(",")
    i = 0
    while i < len(newlist):
        newlist[i] = int(newlist[i])
        i += 1
    return newlist[0] + newlist[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
