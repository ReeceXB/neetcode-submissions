from typing import List

def contains_duplicate(words: List[str]) -> bool:
    i = 0
    while i < len(words):
        if words[i] in set(words[i+1:]):
            return True
        i+=1
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
