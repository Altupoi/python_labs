width = int(input("width = "))
height = int(input("height = "))
outline = input("контур = ")
fill = input("всередині = ")

if height >= 3 or width >= 3:
    for i in range(1,height+1):
        for j in range(1, width + 1):
            if i == 1 or i == height or j == 1 or j == width:
                print(outline,end = "")
            else:
                print(fill,end = "")
        print()
else:
    print("Помилка, занадто малі значення")