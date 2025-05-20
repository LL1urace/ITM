# Практика:

# 13. Найти факториалы чисел от 1 до 5 (включительно).
def find_factorial() -> None:
    """Находит факториалы чисел от 1 до 5 (включительно)."""
    for f in range(1, 6):
        print("Значение:", f, end=" => ")
        for j in range(1, f):
            f *= j
        print("Факториал:", f)



if __name__ == "__main__":
    find_factorial()