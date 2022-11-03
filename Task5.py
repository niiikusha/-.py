# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#5.6 Задачи
#1. Fizz Buzz
print("1. Задание Fizz Buzz")
number = int(input("Введите целое положительное число: "))
if (number % 3 == 0) and (number % 5 == 0):
    print('Fizz Buzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(str(number))
#2. Оценка числа
print("2. Оценка числа")
number = int(input("Введите целое положительное число: "))
if number % 2 != 0:
    print("Плохо")
elif 2 <= number <=  5:
    print("Неплохо")
elif 6 <= number <= 20:
    print("Так себе")
elif number > 20:
    print("Отлично")
#3. Последовательность
print("3. Последовательность")
N = int(input("Введите N от 1 до 9: "))
for i in range(1, N+1):
    print(i, end='')
#4. Секретное сообщение
print('\n4. Секретное сообщение')
stroka = input("Введите секретное сообщение: ")
for i in stroka:
    if i.isupper():
        print(i, end='')
#5. Три слова
print("5. Три слова")
stroka = input("Введите строку ")
k3 = 0
for i in stroka.split():
    if i.isalpha():
        k3 += 1
    else:
        k3 = 0
    if k3 == 3:
        print("True")
if k3 < 3:
    print("False")
#6
print("6. Мир захватили левши")
stroka = ["left", "right", "left", "stop", "bright aright", "ok"]
stroka1 = ', '.join(stroka)
print(stroka1.replace('right', 'left'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
