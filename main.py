# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#1 задание

print("Первое задание")
Array = [10, 2, 3, 3, 3, 4, 5, 6, 6, 10]

for i in range(len(Array)):
    if Array.count(Array[i]) == 1:
        Array[i] = "*"

for i in range(Array.count("*")):
    Array.remove("*")

print(Array)

#2 Задание

print("Второе задание")
x = '1'
y = '0'
z = '0'
n = 2
x_y_z = x

if x != y:
    x_y_z += y

if x != z and y != z:
    x_y_z += z

array = [[x1, y1, z1] for x1 in x_y_z for y1 in x_y_z for z1 in x_y_z if int(x1) + int(y1) + int(z1) != n]

print(array)

#3 Задание

print("Третье задание")

n = 5
array = [x * 2 for x in range(n) if x % 2 != 0]

print(array)

#4 задание

print("4 Задание")

reshotka = [
   'X...',
   '..X.',
   'X..X',
   '....']

shifr = [
   'itdf',
   'gdce',
   'aton',
   'qrdi']

parol = ''
array = []
resh_string = ''.join(reshotka)
sh_string = ''.join(shifr)
numrows = len(reshotka)
resh_string1 = ''

for j in range(4):
    array += [y for x, y in zip(resh_string, sh_string) if x == 'X']
    resh_string1 = ''
    for i in range(4):
        resh_string1 += resh_string[-numrows + i] + resh_string[-numrows*2 + i] + resh_string[-numrows*3 + i] + resh_string[-numrows*4 + i]
    resh_string = resh_string1

print(array)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
