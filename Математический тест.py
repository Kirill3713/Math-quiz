import colorama
from generate_math_question import generate_math_question
from check_answer import check_answer
lightgreen = colorama.Fore.LIGHTGREEN_EX
reset = colorama.Fore.RESET

lightwhite = colorama.Fore.LIGHTWHITE_EX
red = colorama.Fore.RED
green = colorama.Fore.GREEN
light_yellow = colorama.Fore.LIGHTYELLOW_EX
light_magenta = colorama.Fore.LIGHTMAGENTA_EX

def generate_quiz(number_of_questions: int = 10) -> None:
    """Функция для генерации математического теста"""
    correct_answers = 0
    for i in range(number_of_questions):

        primer = generate_math_question()
        print(primer, end= " = ")
        answer = input()
        if check_answer(primer, answer) == True:
            correct_answers += 1
    # Выводим оценку
    if correct_answers == number_of_questions:
        print(green + "Вы отлично справились с тестом! У Вас оценка 5+!👏👏👏")
    elif correct_answers >= number_of_questions * 0.8:
        print(green + "Молодец! Ты написал тест на оценку 5!")
    elif correct_answers >= number_of_questions * 0.6:
        print(light_yellow + "Ваш уровень знаний соответствует оценке 4.")
    elif correct_answers >= number_of_questions * 0.4:
        print(light_magenta + "Вы сдали тест на оценку 3. Надо улучшить результат)")
    elif correct_answers >= number_of_questions * 0.2:
        print(red + "Вы сдали тест на двойку. Подучите - ка устный счет и возвращайтесь на перездачу!")
    else:
        print(red + "Поздравляю, Шарик! Ты - болбес! Вы вообще не умеете считать!")


print(lightgreen + "Добро пожаловать в математический тест!" + reset)
print(lightgreen + "Отвечайте на вопросы и Вы получите оценку!" + lightwhite)
generate_quiz()

