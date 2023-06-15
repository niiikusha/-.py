# 1 задание

N = '123456789'

def reverse(N):
    n_list = list(N)
    n_list.reverse()
    return n_list  # Press Ctrl+F8 to toggle the breakpoint.

print('1 Задание', reverse(N))

#2 Задание

word = 'lol'

def palindrom(Word):
    if Word == Word[::-1]:
        return True
    else:
        return False

print('\n2 Задание', palindrom(word))

#3 Задание

students = [
    {'Фамилия': 'Иванов', 'Имя': 'Иван', 'Отчество': 'Иванович', 'дата рождения': 2000,
     'курс': 2, 'группа': 441, 'Оценки': [4, 5, 3, 4, 5]},
    {'Фамилия': 'Петров', 'Имя': 'Петр', 'Отчество': 'Петрович', 'дата рождения': 2001,
     'курс': 3, 'группа': 442, 'Оценки': [5, 4, 5, 5, 4]},
    {'Фамилия': 'Сидоров', 'Имя': 'Алексей', 'Отчество': 'Николаевич', 'дата рождения': 2002,
     'курс': 2, 'группа': 440, 'Оценки': [3, 3, 4, 4, 5]},
    {'Фамилия': 'Смирнова', 'Имя': 'Мария', 'Отчество': 'Алексеевна', 'дата рождения': 2000,
     'курс': 2, 'группа': 442, 'Оценки': [5, 5, 5, 4, 5]},
    {'Фамилия': 'Павлов', 'Имя': 'Николай', 'Отчество': 'Иванович', 'дата рождения': 2001,
     'курс': 3, 'группа': 440, 'Оценки': [4, 4, 3, 4, 3]}
]

# Возвращает список студентов по курсу
def get_students_by_course(students, course):
    course_students = [student for student in students if student['курс'] == course]
    sorted_students = sorted(course_students, key=lambda s: s['Фамилия'])
    return sorted_students

print('\n3 Задание \nСписок студентов по курсу', get_students_by_course(students, 2))

#Возвращает средние оценки по группам
def calculate_average_scores_by_group(students):
    groups = {}
    for student in students:
        group = student['группа']
        scores = student['Оценки']

        # создаем пустой список оценок по группам
        if group not in groups:
            groups[group] = [0] * len(scores)

        # Суммируем оценки для каждого предмета
        groups[group] = [g + s for g, s in zip(groups[group], scores)]

    for group in groups:
        group_size = len([student for student in students if student['группа'] == group]) #количество студентов
        groups[group] = [score / group_size for score in groups[group]]

    return groups

print('\nСредние оценки группы', calculate_average_scores_by_group(students))

#Младший и старший студент
def find_oldest_and_youngest_students(students):
    oldest_student = min(students, key=lambda s: s['дата рождения'])
    youngest_student = max(students, key=lambda s: s['дата рождения'])
    return oldest_student, youngest_student

print('\nМладший и старший студент', find_oldest_and_youngest_students(students))

#Лучший студент группы
def find_best_student_by_group(students):
    groups = {}

    for student in students:
        group = student['группа']
        scores = student['Оценки']

        if group not in groups:
            groups[group] = student
        else:
            current_best_student = groups[group]
            current_best_average = sum(current_best_student['Оценки']) / len(current_best_student['Оценки'])
            current_average = sum(scores) / len(scores)
            if current_average > current_best_average:
                groups[group] = student
    return groups

print('\nЛучший студент', find_best_student_by_group(students))

#4 Задание

def count_defended_pawns(pawn_positions):
    defended_count = 0

    for position in pawn_positions:
        row = int(position[1])

        # Вычисление позиции слева от текущей пешки
        left_position = chr(ord(position[0]) - 1) + str(row - 1)

        # Вычисление позиции справа от текущей пешки
        right_position = chr(ord(position[0]) + 1) + str(row - 1)

        if left_position in pawn_positions or right_position in pawn_positions:
            defended_count += 1

    return defended_count

pawn_positions1 = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
defended1 = count_defended_pawns(pawn_positions1)

print('\n4 Задание. \nКол-во защищенных пешек', defended1)