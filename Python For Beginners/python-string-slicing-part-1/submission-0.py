def get_substring(input_string: str, start: int, end: int) -> str:
    result = ""
    if end > len(input_string):
        return ""
    for i in range(start+1,end):
        result += input_string[i-1]
    result += input_string[end-1]
    return result


# do not modify below this line
print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
