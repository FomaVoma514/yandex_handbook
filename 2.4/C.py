'''
Новогоднее настроение
Великий математик Виталий Евгеньевич каждый Новый год проводит на работе. Коллеги всегда любили и ценили его, поэтому в этом году решили сделать ему сюрприз — украсить кабинет учёного математическими ёлками. Помогите математикам и напишите программу, которая по введённому числу строит математическую ёлку.

Формат ввода
Вводится одно натуральное число — количество чисел в математической ёлке.

Формат вывода
Требуемая новогодня ёлка.
'''

num = int(input())
current_row = 1
for i in range(1, num + 1):
    print(i, end=' ')
    if i == current_row * (current_row + 1) // 2:
        print()
        current_row += 1
