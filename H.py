'''
Наказание
Наше развлечение не осталось незамеченным...
И наказание нам выбрали соответствующее.

Формат ввода
В первой строке записано одно натуральное число N
Во второй строке записана часть наказания.

Формат вывода
N строк вида: Я больше никогда не буду писать "<часть наказания>"!
'''

n = int(input())
string = input()
for i in range(n):
    print("Я больше никогда не буду писать " + '"' + string + '"' + '!', end='\n')
