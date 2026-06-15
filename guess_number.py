import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7


def read_guess(attempt: int) -> int:
    """Считывает число пользователя и проверяет корректность ввода."""
    while True:
        user_input = input(f"Попытка {attempt}/{MAX_ATTEMPTS}. Введите число: ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue

        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print(f"Ошибка: число должно быть от {MIN_NUMBER} до {MAX_NUMBER}.")
            continue

        return guess


def play_game() -> None:
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    print("Игра 'Угадай число'")
    print(f"Я загадал число от {MIN_NUMBER} до {MAX_NUMBER}.")
    print(f"У вас есть {MAX_ATTEMPTS} попыток.\n")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = read_guess(attempt)

        if guess == secret_number:
            print("Поздравляю, вы угадали число!")
            return
        elif guess < secret_number:
            print("Слишком маленькое число.\n")
        else:
            print("Слишком большое число.\n")

    print(f"Попытки закончились. Было загадано число {secret_number}.")


def main() -> None:
    while True:
        play_game()
        again = input("Сыграть еще раз? (д/н): ").strip().lower()
        if again != "д":
            print("Игра завершена.")
            break


if __name__ == "__main__":
    main()
