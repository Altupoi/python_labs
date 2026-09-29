a = int(input("Введіть ціле число: "))

if a%2==0:
    print("Парне")
else:
    print("Непарне")

age = int(input("Ваш вік: "))

if age>=18:
    print("Ви повнолітні!")
else:
    print("Ви неповнолітні!")

r = int(input("Радіус кола: "))

print("Периметр:", 2*3.14*r)
print("Площа:", 3.14*r**2)

a = int(input("Число a: "))
b = int(input("Число b: "))

if a>b:
    print("a більше")
elif a<b:
    print("b більше")
else:
    print("Числа однакові")