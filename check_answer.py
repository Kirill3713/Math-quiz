def check_answer(primer: str, answer: int) -> bool:
    """Функция для проверки ответа"""
    try:
        answer = float()

        if eval(primer) == answer:
            return True
        else:
            return False
    except ValueError:
        print("Введено некорректное значение.")
if __name__ == "__main__":

    print(check_answer("2 + 3", 5))
    print(check_answer("5 * 3", 10))
    print(check_answer("10-3", "семь"))