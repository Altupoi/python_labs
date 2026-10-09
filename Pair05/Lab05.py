#1
# def CircleArea(r):
#     pi = 3.14159
#     area = pi * r**2
#     return area
#
# def RectArea(a,b):
#     area = a*b
#     return area
#
# def TriangleArea(h,a):
#     area = h*a/2
#     return area
#
# def main():
#     result = 0
#     if Shape == "круг":
#         r = int(input("Радіус: "))
#         result = CircleArea(r)
#     elif Shape == "прямокутник":
#         a = int(input("Ширина: "))
#         b = int(input("Висота: "))
#         result = RectArea(a,b)
#     elif Shape == "трикутник":
#         h = int(input("Висота: "))
#         a = int(input("Сторона прилегла до висоти: "))
#         result = TriangleArea(h,a)
#     print("Площа " + Shape + "а:",result)
#
# Shape = input("Фігура: ").strip().lower()
# main()

#2
# def is_prime(n):
#     check = True
#     for i in range(2, n):
#         if n % i == 0:
#             check = False
#     if check and n > 0:
#         return "так"
#     else:
#         return "ні"
#
# def divisors(n):
#     dvs = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             dvs.append(i)
#     return dvs
#
# def digit_sum(n):
#     s = 0
#     while n > 0:
#         s += n%10
#         n//=10
#     return s
#
# def main(n):
#     print("Просте число:", is_prime(n))
#     print("Дільники:", divisors(n))
#     print("Сума цифр:", digit_sum(n))
#
# main(int(input("N = ")))

#3
# def average(grades):
#     return sum(grades) / len(grades)
# def minimum(grades):
#     return min(grades)
# def maximum(grades):
#     return max(grades)
# def count_above(grades,value):
#     count = 0
#     for grade in grades:
#         if grade > value:
#             count += 1
#     return count
# def main(grades,value):
#     print("Середній бал:",average(grades))
#     print("Мінімальна:",minimum(grades))
#     print("Максимальна:",maximum(grades))
#     print("Вище "+str(value)+":",count_above(grades,value))
#
# Grades = input("Оцінки: ").strip().strip("[").strip("]").split(",")
# for i in range(len(Grades)): Grades[i] = int(Grades[i].strip())
# Value = int(input("Поріг: "))
# main(Grades,Value)

#4
# def check_length(password):
#     if len(password) < 8:
#         return False
#     else:
#         return True
# def check_number(password):
#     check = False
#     for char in password:
#         if char.isdigit():
#             check = True
#     return check
# def check_upper(password):
#     check = False
#     for char in password:
#         if char.isupper():
#             check = True
#     return check
# def check_lower(password):
#     check = False
#     for char in password:
#         if char.islower():
#             check = True
#     return check
# def check_sym(password):
#     check = False
#     for char in password:
#         if not char.isdigit() and not char.isalnum():
#             check = True
#     return check
# def main(password):
#     reason = ""
#     check = True
#     if not check_length(password):
#         check = False
#         reason = "не достатньо довгий"
#     if not check_upper(password):
#         check = False
#         reason = "немає великої літери"
#     if not check_lower(password):
#         check = False
#         reason = "немає малої літери"
#     if not check_sym(password):
#         check = False
#         reason = "немає спеціального символу"
#     if check:
#         print("Пароль відповідає вимогам.")
#     else:
#         print("Пароль не відповідає вимогам.")
#         print("Не виконано:",reason)
#
# main(input("Password: "))