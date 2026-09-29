N = int(input("Кількість поїздок в пасажира:"))
k = int(input("Квитків в пачці:"))
p1 = int(input("Ціна за 1 квиток:"))
p2 = int(input("Ціна за пачку квитків:"))

SumDown = N%k * p1 + int(N/k) * p2
SumUp = (int(N/k) + 1) * p2

print("Оптимальні витрати:",min(SumDown,SumUp))