N = int(input("Введіть число: "))

sum = 0
count = 0
for i in range(1,N+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        count += 1

print("Кількість:",count)
print("Сума:",sum)
print("Середнє:",sum/count)