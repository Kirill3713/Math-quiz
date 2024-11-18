# Импортируем модули
import random
# Создаем функцию
def generate_math_question(a: int = 1, b: int = 10) -> str:
    """
    Функция для генерации примера
    """
    # Создаем список операторов
    operators = ['+', '-', '*', '/']
    # Выбираем случайные числа из заданного диапазона и оператор
    num1, num2 = random.randint(a, b), random.randint(a, b)
    operator = random.choice(operators)
    # Проверяем чтобы деление было только нацело
    if operator == '/':
        num1 = num2*num1
    # Создаем пример
    primer = f"{num1} {operator} {num2}"
    # Возвращаем пример
    return primer
# Точка входа
if __name__ == "__main__":
    print(generate_math_question())
    print(generate_math_question(9, 111))