# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#1
print("1 Задание")
name = input("Введите свое имя: ")
print(f"Hello {name}! You just delved into Python. Great start!")  # Press Ctrl+F8 to toggle the breakpoint.
#2
print("2 Задание")
thickness = int(input("Введите толщину маркера "))
c = input("Введите маркер ")
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
#3
print("3 Задание")
text = input("Введите заголовок: ")
print(text.title())
#4
print("4 Задание")
amount = int(input("Введите число: "))
if amount > 0:
    print('{0:,}'.format(amount))
else:
    print("Введите число больше 0")
#5
print("5 Задание")
H = int(input("Введите ширину ковра: "))
W = 3 * H
for i in range(H):
    if i == H//2:
        print('WELCOME'.center(W, '='), end='')
    else:
        if W % 2 == 0:
            print('+=' * (W//2), end='')
        else:
            print('+=' * (W//2) + '+', end='')
    print()
#6
print("6 Задание")
number = int(input("Введите ЦЕЛОЕ число: "))
num = 1
while number != 0:
    if number % 10 != 0:
        num *= number % 10
    number //= 10
print(num)
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
