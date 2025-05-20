# 4.
# Условие:
# Функция reverse_words(text: str) -> str
# меняет порядок слов в строке на обратный.
# Пример:
# reverse_words("hello world today") → "today world hello"

def reverse_words(text: str) -> str:
    slices = text.split()
    reverse_list = []
    print(slices)
    for word in range(len(slices)-1, -1, -1):
        reverse_list.append(slices[word])
    reverse_str = " ".join(reverse_list)
    return reverse_str



if __name__ == "__main__":
    my_text = "hello world today"
    my_reverse_text = reverse_words
    print(my_reverse_text(my_text))

# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
#
# Example 1:
#
# Input: s = "[]"
#
# Output: true
# Example 2:
#
# Input: s = "([{}])"
#
# Output: true
# Example 3:
#
# Input: s = "[(])