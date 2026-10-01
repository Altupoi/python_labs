N = int(input("Введіть число: "))

count = 1
sum = N % 10
big = N % 10
small = N % 10
N //= 10

while N > 0:
    i = N % 10
    if big < i:
        big = i
    if small > i:
        small = i
    sum += i
    count += 1
    N //= 10

print("Кількість цифр:", count)
print("Сума цифр:", sum)
print("Найбільша цифра:", big)
print("Найменша цифра:", small)