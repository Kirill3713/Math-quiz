import random
import colorama
lightwhite = colorama.Fore.LIGHTWHITE_EX
black = colorama.Fore.BLACK


def generate_math_question(a: int = 1, b: int = 10) -> list:
    """Функция для генерации примера"""
    operators = ['+', '-', '*', '/']

    num1, num2 = random.randint(a, b), random.randint(a, b)
    operator = random.choice(operators)
    if operator == '/':
        num1 = num2*num1


    primer = f"{num1} {operator} {num2}"
    return primer


if __name__ == "__main__":

    print(generate_math_question())

    print(generate_math_question(9, 111))
