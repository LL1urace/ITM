# Условие:
# Функция is_palindrome(s: str) -> bool проверяет, является ли строка палиндромом (без учёта пробелов и регистра).
#
# Пример:
# is_palindrome("A man a plan a canal Panama") → True
def is_palindrome(s: str) -> bool:
    reverse_word = "".join(reversed(s))
    reverse_word = reverse_word.replace(" ", "")
    reverse_word = reverse_word.lower()
    reverse_word = "".join(reverse_word)
    reverse_word.lower()
    s = s.lower()
    s = s.replace(" ", "")
    if reverse_word == s:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))
    print(is_palindrome("hello"))
    print(is_palindrome("mama"))
    print(is_palindrome("казак"))
    print(is_palindrome("A man a plan a canal Panama"))