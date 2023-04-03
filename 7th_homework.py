# """
# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в
# программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке
# """
#
# poem = str(input('Вводи стих, медоед: '))
# vowel_letters = 'ауоыиэяюёе'
#
#
# def poem_test(poem: str) -> str:
#     vowel = []
#     for i in range(len(poem)):
#         if poem[i] in vowel_letters:
#             vowel.append(1)  # В качестве гласных в списке будут 1
#         elif poem[i] == ' ':
#             vowel.append(2) # В качестве пробелов в списке будут 2
#     if vowel.count(1) % (vowel.count(2) + 1) == 0:
#         return 'Парам пам пам'
#     else:
#         return 'Пам парам'
#
#
# print(poem_test(poem))
#
# """
# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6,
# num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую
# элемент по номеру строки и столбца. Аргументы num_rows и num_columns
# указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
# """
#
# lines = int(input('Введите число строк: '))
# columns = int(input('Введите число столбцов: '))
#
#
# def print_operation_table(lines, columns):
#     line1 = [i for i in range(1, columns + 1)]
#     for i in range(lines):
#         print(*line1)
#         for j in range(len(line1)):
#             line1[j] += j + 1
#     return 'Таблица готова'
#
#
# print(print_operation_table(lines, columns))
