import math


def read_positive_integer() -> int:
    """Запрашивает у пользователя положительное целое число."""
    while True:
        user_input = input("Введите положительное целое число: ").strip()

        try:
            number = int(user_input)
        except ValueError:
            print("Ошибка: нужно ввести именно целое число.")
            continue

        if number <= 0:
            print("Ошибка: число должно быть положительным, то есть больше нуля.")
            continue

        return number


def calculate_factorial(number: int) -> int:
    """Вычисляет факториал числа с помощью оптимизированной функции math.factorial."""
    return math.factorial(number)


def main() -> None:
    number = read_positive_integer()
    result = calculate_factorial(number)
    print(f"Факториал числа {number} равен {result}")


if __name__ == "__main__":
    main()
