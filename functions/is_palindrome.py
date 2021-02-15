def is_palindrome(string: str) -> bool:
    return string[::-1].casefold() == string.casefold()


print(is_palindrome("racecar"))
print(is_palindrome("cat"))
print(is_palindrome("Radar"))
