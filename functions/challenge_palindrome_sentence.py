def is_palindrome(string: str) -> bool:
    return string[::-1].casefold() == string.casefold()


def is_sentence_palindrome(sentence: str) -> bool:
    string = ""

    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string)


print(is_sentence_palindrome("Was it a car, or a cat, I saw"))
