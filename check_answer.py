# Создаем функцию
def check_answer(primer: str, answer: int) -> bool:
    """
    Функция для проверки ответа
    """
    try:
        # Проверяем ответ с помощью функции eval()
        if eval(primer) == float(answer):
            return True
        else:
            return False
    except ValueError:
        # Создаем исключение на случай неправильного ввода
        print("Введено некорректное значение.")
# Точка входа
if __name__ == "__main__":
    print(check_answer("2 + 3", 5))
    print(check_answer("5 * 3", 10))
    print(check_answer("10-3", "семь"))