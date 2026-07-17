from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    newdict = {}
    i = 0
    while i < len(word):
        if(word[i:i+1] in newdict):
            newdict[word[i:i+1]] += 1
        else:
            newdict[word[i:i+1]] = 1
        i+=1
    return newdict
            

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
