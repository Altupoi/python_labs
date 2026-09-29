coordinates = input('Введіть кординати (в форматі "x y"):')
x,y = coordinates.split(" ")
x = int(x)
y = int(y)

if x>0 and y>0:
    print("I чверть")
elif x<0 and y>0:
    print("II чверть")
elif x<0 and y<0:
    print("III чверть")
elif x>0 and y<0:
    print("IV чверть")
else:
    print("На одній з осей")