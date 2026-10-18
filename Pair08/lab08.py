#1
# a = input("A: ")
# b = input("B: ")
# operation = input("Операція: ")
# try:
#     a = int(a)
#     b = int(b)
#     if operation == "+":
#         print(a + b)
#     elif operation == "-":
#         print(a - b)
#     elif operation == "*":
#         print(a * b)
#     elif operation == "/":
#         print(a / b)
#     else:
#         raise ValueError("oper")
# except ValueError as error:
#     if str(error) == "oper":
#         print("Помилка: не правильна операція")
#     else:
#         print("Помилка: потрібно ввести цілі числа.")
# except ZeroDivisionError:
#     print("Помилка: на нуль ділити не можна.")
from pstats import func_get_function_name

#2
# grade = 0
# while True:
#     try:
#         grade = int(input("Оцінка: "))
#         if grade < 0 or grade > 12:
#             raise ValueError("bounds")
#     except ValueError as error:
#         if str(error) == "bounds":
#             print("Помилка: оцінка повинна бути від 1 до 12.")
#         else:
#             print("Помилка: потрібно ввести ціле число.")
#     else:
#         print(f'Прийнято: {grade}')
#         break

#3
# Students = [
#     "Олександр Коваленко",
#     "Коваль Владислав",
#     "Максим Ткаченко",
#     "Анна Шевченко",
#     "Артем Бондаренко"
# ]
# Grades = {
#     "Зарубіжна література": 12,
#     "Захист України": 11,
#     "Алгебра": 8,
#     "Геометрія": 10,
#     "Інформатика": 2
# }
# operation = input("1 - учень, 2 - предмет: ")
# if operation == "1":
#     indx = 0
#     try:
#         indx = int(input("Індекс: "))
#         print(Students[indx])
#     except ValueError:
#         print("Помилка: потрібно ввести ціле число.")
#     except IndexError:
#         print("Помилка: учня з таким індексом немає.")
# elif operation == "2":
#     name = 0
#     try:
#         name = input("Назва: ")
#         print(Grades[name])
#     except KeyError:
#         print("Помилка: такий предмет відсутній.")
# else:
#     print("Помилка: не обрана дія.")

#4
# data = {}
# try:
#     with open("students.txt", "r", encoding="utf-8") as file:
#         WrongCount = 0
#         lines = file.readlines()
#         for i,line in enumerate(lines):
#             try:
#                 vals = line.strip().split(";")
#                 if(len(vals)!=2):
#                     raise ValueError("ValCount")
#                 name = vals[0]
#                 grade = int(vals[1])
#                 if grade < 0 or grade > 100:
#                     raise ValueError("GradeLimit")
#                 data[name] = grade
#             except ValueError as error:
#                 if str(error) == "GradeLimit":
#                     print(f'Рядок {i+1} пропущено: бал поза діапазоном.')
#                     WrongCount+=1
#                 elif str(error) == "ValCount":
#                     print(f'Рядок {i+1} пропущено: неправильний формат.')
#                     WrongCount += 1
#                 else:
#                     print(f'Рядок {i+1} пропущено: бал не є цілим числом.')
#                     WrongCount += 1
#         print(f'Правильних записів: {len(lines)-WrongCount}')
#         print(f'Пропущено: {WrongCount}')
# except FileNotFoundError:
#     print("Помилка: відсутній файл")
#
# with open("result.txt", "w", encoding="utf-8") as file:
#     checkedGrades = []
#     curGrade = 0
#     i = 0
#     for n,g in data.items():
#         fname = n
#         for name,grade in data.items():
#             if not name in checkedGrades:
#                 if curGrade < grade:
#                     curGrade = grade
#                     fname = name
#         checkedGrades.append(fname)
#         print(f"{fname};{data[fname]}", file=file)
#         curGrade = 0
#         i += 1