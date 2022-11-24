# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#1 задание
print("1 задание")
text = "hello, word of word"
chars_popularity = {}
words_popularity = {}
good_text = " "

for i in text:
    if i.isalpha() or i == ' ':
        good_text += i
print(good_text)

for i in good_text:
    if i != ' ':
        chars_popularity[i] = good_text.count(i)
print(chars_popularity)

for i in good_text.split():
    words_popularity[i] = good_text.count(i)
print(words_popularity)

#2 задание
print("2 Задание")
number = int(input("Введите целое число от 1 до 3999: "))
RIM = zip( [1000,900,500,400,100,90,50,40,10,9,5,4,1],
           ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"] )
result = ''
for i, j in RIM:
    while number >= i:
        result += j
        number -= i
print("Результат:", result)
#3 Задание
print("3 Задание")
banks = {62.25: "Открытие", 59.96:"Сбербанк", 60.8:"ВТБ Банк"}
best_bank = min(banks.keys())
print(best_bank, banks[best_bank])
#4 Задание
print("4 Задание")
book = {'Petr': '546810', 'Katya': '241815'}
inverse_dict = {}
for k, v in book.items():
    inverse_dict[v] = k
print(inverse_dict)
#5 Задание
print("5 Задание")
dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]
DatesAndRates = dict(zip(dates, rates))
print(DatesAndRates)
#6 Задание
print('6 Задание')

data = [
    "00X",
    "X0.",
    ".00"
 ]
Result = 'Ничья'
otvet = 0
# проверка по диагоналям
if (data[0][0] == data[1][1] and data[0][0] == data[2][2]) or (data[0][2] == data[1][1] and data[0][0] == data[2][0]):
    Result = data[1][1]
    otvet = 1
# если победитель нашелся на диагоналях пропускаем весь остальной цикл
if otvet == 0:
    for i in range(len(data)): # проверка по вертикали
        if data[0][i] == data[1][i] and data[0][i] == data[2][i] and data[0][i] != '.':
            Result = data[0][i]
            break
        if data[i] == 'XXX' or data[i] == '000': #  проверка по горизонтали
            Result = data[i][0]
            break

print('->', Result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
