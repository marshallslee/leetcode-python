def is_palindrome(x: int) -> bool:
    val = str(x)
    return val == val[::-1]


print(is_palindrome(3903))
