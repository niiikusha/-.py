# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#4.6 Задачи
#1. Среднее
from random import randint
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
srednee = (a + b + c)/3
#print(a, b, c)
print("1. Задание\nСреднее = ", srednee)
#2. Деление и еще раз деление
a = randint(0, 100)
b = randint(0, 100)
delenie = a // b
ostatok = a % b
print("2. Задание\nЦелочисленное деление = ", delenie, "\nОстаток = ", ostatok)
#3. Округление
print("3. Задание")
number = float(input("Введите дробное число: "))
print(f"1) {number:.2f}\n" f"2) {number:.0f}\n" f"3) {number:=011}")
#4. Число "наоборот"
print("4. Задание")
number = input("Введите целое число: ")
if int(number) < 0:
    reverse = -(int(number[:0:-1]))
else:
    reverse = int(number[::-1])
print("Обратное = ", reverse)
#5. Число "наоборот" (усложненное)
print("5. Задание")
number = input("Введите целое число: ")
if int(number) < 0:
    reverse = -(int(number[:0:-1]))
else:
    reverse = int(number[::-1])
if -2 ** 31 <= reverse <= 2 ** 31 - 1:
    print(reverse)
else:
    print(0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
