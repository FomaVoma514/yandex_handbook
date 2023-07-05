'''
На старт! Внимание! Марш!
По правилам велогонки, после квалификации каждый гонщик стартует с задержкой на секунду больше, чем у гонщика перед ним.
Первый гонщик стартует на счёт 3. Напишите программу, которая сможет автоматизировать старт всех гонщиков, участвующих в велогонке.

Формат ввода
Вводится одно натуральное число — количество участников велогонки.

Формат вывода
Требуется вывести отсчёт.
'''

num_racers = int(input())

start_time = 3

for i in range(num_racers):
    for j in range(start_time, 0, -1):
        print('До старта', j, 'секунд(ы)')
    print('Старт', i + 1, end='!!!\n')
    start_time += 1
