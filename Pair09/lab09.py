#1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f'{self.width} × {self.height}: площа = {self.area()}, периметр = {self.perimeter()}')
#
# Rectangle(5,3).info()
# Rectangle(10,4).info()

#2
# class Student:
#     def __init__(self, name, grades = []):
#         self.name = name
#         self.grades = grades
#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print(f'Оцінка {grade} не додається.')
#     def average(self):
#         if self.grades:
#             return sum(self.grades) / len(self.grades)
#         else:
#             return 0
#     def __str__(self):
#         return f'{self.name}: {self.grades}, середній = {self.average()}'
#
# ivan = Student("Ivan Petrenko")
# ivan.add_grade(10)
# ivan.add_grade(12)
# ivan.add_grade(15)
# ivan.add_grade(9)
# print(ivan)

#3
# Students = [
#     Student("Anna",[9,11,12]),
#     Student("Ivan",[11,8]),
#     Student("Olha",[12,12,10]),
#     Student("Artem",[12,10,12]),
#     Student("Bogdan",[11,8,12])
# ]
# BestStudents = [Students[0]]
# for student in Students:
#     print(f'{student.name} — {student.average()}')
#     if BestStudents[0].average() < student.average():
#         BestStudents = [student]
#     elif BestStudents[0].average() == student.average():
#         BestStudents.append(student)
# print(f'Найкращий результат:', end=" ")
# for student in BestStudents:
#     print(f'{student.name}',end=" ")
# print(f'— {BestStudents[0].average()}')

#4
# class Wallet:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print(f'Помилка: {amount} має бути додатнім')
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#             else:
#                 print(f'Помилка: недостатньо коштів для {amount}')
#         else:
#             print(f'Помилка: {amount} має бути додатнім')
#     def info(self):
#         print(f'{self.owner}: баланс {self.balance}')
#
# Ivan = Wallet('Ivan',1000)
# Ivan.deposit(500)
# Ivan.withdraw(300)
# Ivan.withdraw(2000)
# Ivan.info()
#
# Olha = Wallet('Olha',700)
# Olha.withdraw(200)
# Olha.deposit(100)
# Olha.info()