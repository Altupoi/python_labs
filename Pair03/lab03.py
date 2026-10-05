#1
# text = input("Введіть довільний текст: ").lower()
#
# ltrs = 0
# nums = 0
# spcs = 0
# vwls = 0
#
# syms = len(text)
# wrds = len(text.split(" "))
# vowels = {'a','e','i','o','u'}
#
# for char in text:
#     if char.isalpha():
#         ltrs+=1
#     if char.isdigit():
#         nums+=1
#     if char == ' ':
#         spcs+=1
#     for i in vowels:
#         if char == i:
#             vwls+=1
#
# print("Символів:", syms)
# print("Літер:", ltrs)
# print("Цифр:", nums)
# print("Пробілів:", spcs)
# print("Голосних:", vwls)
# print("Слів:", wrds)

#2
# name = input("ПІБ: ").lower()
# parts = name.split(" ")
# finished = ""
#
# for part in parts:
#     if part != parts[0]:
#         part = part[0] + "."
#     else:
#         part += " "
#     finished += part.capitalize()
#
# print(finished)

#3
# text1 = input("Введіть слово: ").lower()
# text2 = input("Введіть ще слово: ").lower()
#
# check = True
# for char in text1:
#     check2 = False
#     for char2 in text2:
#         if char == char2:
#             check2 = True
#             break
#     if not check2:
#         check = False
#         break
#
# for char in text2:
#     check2 = False
#     for char2 in text1:
#         if char == char2:
#             check2 = True
#             break
#     if not check2:
#         check = False
#         break
#
# if check:
#     print("Слова є анаграмами.")
# else:
#     print("Слова не є анаграмами.")

#4
# text = input("Введіть речення: ").strip()
# words = text.split(" ")
#
# biggest = words[0]
# smallest = words[0]
# UniqueWrds = 0
# for i in range(0,len(words)):
#     word = words[i].lower()
#
#     if len(word) > len(biggest.split(" ")[0]):
#         biggest = word
#     elif len(word) == len(biggest.split(" ")[0]):
#         check = True
#         for UnqWord in biggest.split(" "):
#             if word == UnqWord.lower():
#                 check = False
#                 break
#         if check:
#             biggest += " " + word
#
#     if len(word) < len(smallest.split(" ")[0]):
#         smallest = word
#     elif len(word) == len(smallest.split(" ")[0]):
#         check = True
#         for UnqWord in smallest.split(" "):
#             if word == UnqWord.lower():
#                 check = False
#                 break
#         if check:
#             smallest += " " + word
#
#     check = True
#     for UnqWord in words[:i]:
#         if word == UnqWord.lower():
#             check = False
#             break
#     if check:
#         UniqueWrds += 1
#
# print("Найдовші:",biggest)
# print("Найкоротші:",smallest)
# print("Унікальних слів:", UniqueWrds)
#
# From = input("Введіть слово для заміни: ").lower().strip()
# To = input("Введіть змінене слово: ")
# EditedText = ""
# for word in words:
#     if word.lower() == From:
#         EditedText += To + " "
#     else:
#         EditedText += word + " "
# EditedText = EditedText[:-1]
#
# print("Після зміни:",EditedText)