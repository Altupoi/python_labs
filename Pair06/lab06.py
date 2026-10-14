#1
# from math import *
# r = int(input("Радіус: "))
# a = input("Катети: ").strip().split(",")
# for i in range(len(a)): a[i] = int(a[i].strip())
# items = int(input("Предметів: "))
# fit = int(input("В упаковці: "))
#
# S = pi * r ** 2
# print("Площа круга:",round(S,2))
# b = sqrt(a[0]**2 + a[1]**2)
# print("Гіпотенуза:",b)
# packets = ceil(items / fit)
# print("Потрібно упаковок:",packets)

#2
# import random
# from operator import countOf
# from statistics import *
#
# N = int(input("N = "))
#
# grades = []
# for i in range(N): grades.append(random.randint(1,12))
# print("Оцінки:",grades)
# print("Min:",min(grades))
# print("Max:",max(grades))
# print("Середнє:",mean(grades))
# print("Медіана:",median(grades))
# total = 0
# for grade in grades:
#     if grade >= 10 and grade <= 12:
#         total += 1
# print("Оцінок 10-12:",total)

#3
# from datetime import *
# Current = date.today()
# Event = input("Дата події: ").strip().split("-")
# for i in range(len(Event)): Event[i] = int(Event[i].strip())
# Event = date(Event[0],Event[1],Event[2])
# if(Current > Event):
#     print(f'Подія відбулася {(Current-Event).days} днів тому')
# elif(Current < Event):
#     print(f'До події залишилося: {(Event-Current).days} днів')
# else:
#     print("Подія сьогодні!")
