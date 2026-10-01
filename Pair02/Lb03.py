N = int(input("Введіть число: "))

for i in range(1,N):
    flag = 0
    count = 0
    num = i
    while num > 0:
        n = num % 10
        if not n == 0 and i % n == 0 : flag += 1
        num //= 10
        count += 1
    if flag == count: print(i,end = " ")