#1
# Slist = input("Введіть список чисел: ").strip("[").strip("]").split(",")
# for i in range(len(Slist)):
#     Slist[i] = int(Slist[i])
#
# PosList = []
# NegList = []
# ParList = []
# By3List = []
# for i in Slist:
#     if i >= 0:
#         PosList.append(i)
#     elif i < 0:
#         NegList.append(i)
#     if i % 2 == 0:
#         ParList.append(i)
#     if i % 3 == 0:
#         By3List.append(i)
#
# MaxVal = max(Slist)
# MinVal = min(Slist)
# Sum = sum(Slist)
# Avg = sum(Slist)/len(Slist)
#
# print("Додатні:",PosList)
# print("Від’ємні:",NegList)
# print("Парні:",ParList)
# print("Кратні 3:",By3List)
# print("Min:", MinVal, "Max:", MaxVal, "Sum:",Sum, "Average:", Avg)

#2
# group1 = input("group1 = ").strip().strip("{").strip("}").split(",")
# for i in range(len(group1)): group1[i] = group1[i].strip().strip("'")
# group1 = set(group1)
#
# group2 = input("group2 = ").strip().strip("{").strip("}").split(",")
# for i in range(len(group2)): group2[i] = group2[i].strip().strip("'")
# group2 = set(group2)
#
# SharedGroup = ", ".join(group1 & group2)
# JGroup1 = ", ".join(group1 - group2)
# JGroup2 = ", ".join(group2 - group1)
# Everyone = ", ".join(group1 | group2)
# print("Спільні:", SharedGroup)
# print("Тільки group1:", JGroup1)
# print("Тільки group2:", JGroup2)
# print("Усі:", Everyone)

#3
# Products = {
#     "paper": 20,
#     "sugar": 30,
#     "milk": 48,
#     "tea": 75,
#     "coffee": 80,
#     "eggs": 100
# }
# print(Products)

#Додавання нового товару/зміна ціни існуючого

# Name = input("Назва товару: ")
# Price = int(input("Ціна товару: "))
# Products.update({Name:Price})
# print(Products)

#Пошук товару за назвою

# Name = input("Назва товару: ")
# if Products.get(Name):
#     print(Name+"-"+str(Products.get(Name)))
# else:
#     print("Товар не знайдено")

# виведення всіх товарів в діапазоні

# Range = input("Ціновий діапазон: ").split("..")
# MinV = int(Range[0])
# MaxV = int(Range[1].strip("грн"))
# for name,price in Products.items():
#     if price >= MinV and price <= MaxV:
#         print(name + "-" + str(price) + "грн")

#4
# StudentData = {}
# Group_info = input("group_info = ").strip().strip("(").strip(")").split(",")
# for i in range(len(Group_info)): Group_info[i] = Group_info[i].strip().strip("'")
# Group_info = tuple(Group_info)
#
# while True:
#     #Додавання учня
#     while True:
#         print()
#         data = input("ПІБ та 5 оцінок учня: ").strip().split(":")
#         Name = data[0].strip()
#         Marks = data[1].strip().split(" ")
#         check = True
#         for i in range(len(Marks)):
#             if i > 5:
#                 check = False
#                 break
#             if int(Marks[i]):
#                 Marks[i] = int(Marks[i])
#                 if Marks[i] <= 0 or Marks[i] > 12:
#                     check = False
#                     break
#             else:
#                 check = False
#                 break
#         if check:
#             break
#         else:
#             print("Неправильно введено дані")
#     StudentData.update({Name:Marks})
#     print()
#
#     # Друк усього журналу/середні бали учнів
#     print(" - ".join(Group_info))
#     for name, marks in StudentData.items():
#         avg = sum(marks) / 5
#         print(name + " - ", end="")
#         for i in range(5): print(Marks[i], end=" ")
#         print(" - " + str(avg))
#
#     # Найкращий результат
#     bestGrade = 0
#     for name, marks in StudentData.items():
#         avg = sum(marks)/5
#         if avg > bestGrade:
#             bestGrade = avg
#     print("Найкращий результат: ",end="")
#     for name, marks in StudentData.items():
#         avg = sum(marks)/5
#         if avg == bestGrade:
#             print(name,end=" ")
#     print("- " + str(bestGrade))