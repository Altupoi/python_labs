#1
# with open("text.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     print("Рядків:",len(lines))
#
#     text = ""
#     for line in lines:
#         text += line
#     words = text.split(" ")
#     for i in range(len(words)): words[i] = words[i].strip()
#     print("Слів:",len(words))
#     print("Символів:",len(text))
#
#     bLines = [0]
#     for i in range(len(lines)):
#         if len(lines[bLines[0]]) < len(lines[i]):
#             bLines = [i]
#         elif len(lines[bLines[0]]) == len(lines[i]):
#             bLines.append(i)
#     maxLength = len(lines[bLines[0]])
#     if len(bLines) == 1:
#         print(f'Найдовший рядок: №{bLines[0]}, {maxLength} символів')
#         print("Текст:",lines[i])
#     else:
#         print("Найдовші рядки: ",end="")
#         for i in bLines:
#             print(f'№{i},',end="")
#         print(f'{maxLength} символів')
#         print("Текст:")
#         for i in bLines:
#             print(lines[i])

#2
# Part = input("Фрагмент: ")
# with open("text.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     flag = False
#     for i in range(len(lines)):
#         if Part in lines[i]:
#             print(f'{i}: {lines[i].strip("\n")}')
#             flag = True
#     if not flag:
#         print("Немає збігів.")

#3
# TData = []
# with open("students.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         name, grade = line.split(";")
#         if int(grade) > 80:
#             TData.append([name, int(grade)])
# with open("result.txt", "w", encoding="utf-8") as file:
#     for name, score in TData:
#         print(f"{name};{score}", file=file)

#4
def avg_grade(grades):
    return sum(grades) / len(grades)

Data = []
with open("grades.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        name, subject, grade = line.strip("\n").split(";")
        index = -1
        for i in range(len(Data)):
            if Data[i][0] == name:
                index = i

        if index == -1:
            Data.append([name, grade])
        else:
            Data[index][1] += " "+grade
    for i in range(len(Data)):
        Grades = Data[i][1].split(" ")
        for j in range(len(Grades)): Grades[j] = int(Grades[j])
        Data[i][1] = Grades

with open("report.txt", "w", encoding="utf-8") as file:
    Best = [[Data[0][0],avg_grade(Data[0][1])]]

    for name, grades in Data:
        avg = avg_grade(grades)
        if avg > Best[0][1]:
            Best = [[name, avg]]
        elif avg == Best[0][1] and Best[0][0] != name:
            Best.append([name, avg])

    for i in range(len(Best)):
        print(f"{Best[i][0]} — оцінок: {len(Data[i][1])} — середній: {Best[i][1]}", file=file)
            Best.append([name, avg])
        
