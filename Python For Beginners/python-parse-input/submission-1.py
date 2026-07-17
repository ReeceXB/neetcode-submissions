from typing import List

def read_integers() -> List[int]:
    newlist = input().split(",")
    i = 0
    while i < len(newlist):
        newlist[i] = int(newlist[i])
        i += 1
    return newlist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
