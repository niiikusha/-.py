# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Первое задание
print("Первое задание")
spisok_int = [0, 1, 2, 3, 4, 5]
spisok_chetn = spisok_int[::2]
spisok_chetn_sum = sum(spisok_chetn) * spisok_int[-1]
print("Result", spisok_chetn_sum)
#Второе задание
print("Второе задание")
elements = [10.2, -2.2, 0, 1.1, 0.5]
if elements == []:
    print("0")
else:
    raznica = max(elements)-min(elements)
    print("Result: ", round(raznica, 3))
#Третье задание
print("Третье задание")
elements = (1, 2, 3, 0)
elements_sort = sorted(elements, key=abs)
print("Отсортированный по абсолютному значению: ", elements_sort)
#Четвертое задание
print("Четвертое задание")
elements = [3, 6, 20, 99, 10, 15]
elements_sort = sorted(elements)
dlina = len(elements)
if dlina % 2 == 0:
    mediana = (elements_sort[dlina // 2 - 1] + elements_sort[dlina // 2])/2
else:
    mediana = elements_sort[dlina // 2]
print("Медиана: ", mediana)
#Пятое задание

#spisok_sum = sum
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
