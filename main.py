# Импортируем модули и создаем переменные для цветов
import os
import colorama
from generate_math_question import generate_math_question
from check_answer import check_answer
light_green = colorama.Fore.LIGHTGREEN_EX
reset = colorama.Fore.RESET
light_white = colorama.Fore.LIGHTWHITE_EX
red = colorama.Fore.RED
green = colorama.Fore.GREEN
light_yellow = colorama.Fore.LIGHTYELLOW_EX
light_magenta = colorama.Fore.LIGHTMAGENTA_EX
# Создаем функцию
def generate_quiz(number_of_questions: int = 10) -> None:
    """
    Функция для генерации математического теста
    """
    correct_answers = 0
    # Создаем и выводим вопросы для теста
    for _ in range(number_of_questions):

        primer = generate_math_question()
        print(primer, end= " = ")
        answer = input()
        if check_answer(primer, answer) == True:
            correct_answers += 1
    # Выводим оценку
    if correct_answers == number_of_questions:
        print(green + "Вы отлично справились с тестом! У Вас оценка 5+!👏👏👏" + reset)
    elif correct_answers >= number_of_questions * 0.8:
        print(green + "Молодец! Ты написал тест на оценку 5!" + reset)
    elif correct_answers >= number_of_questions * 0.6:
        print(light_yellow + "Ваш уровень знаний соответствует оценке 4." + reset)
    elif correct_answers >= number_of_questions * 0.4:
        print(light_magenta + "Вы сдали тест на оценку 3. Надо улучшить результат)" + reset)
    elif correct_answers >= number_of_questions * 0.2:
        print(red + "Вы сдали тест на двойку. Подучите - ка устный счет и возвращайтесь на перездачу!" + reset)
    else:
        print(red + "Поздравляю, Шарик! Ты - болбес! Вы вообще не умеете считать!" + reset)
# Точка входа
if __name__ == "__main__":
    # Очистка экрана
    os.system('cls')
    # Приветствие
    print(light_green + "Добро пожаловать в математический тест!" + reset)
    print(light_green + "Отвечайте на вопросы и Вы получите оценку!" + light_white)
    # Вызов функции
    generate_quiz()
    print(green + "Спасибо за прохождение теста!" + reset)