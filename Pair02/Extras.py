height = int(input("height = "))
outline = input("контур = ")
fill = input("всередині = ")

width = 1+(height-1)*2
w = 1
for j in range(1,height+1):
    for i in range(1, width + 1):
        if i >= (width-w)//2+1 and i <= (width-w)//2 + w:
            if i == (width-w)//2+1 or i == (width-w)//2 + w:
                print(outline,end = "")
            elif j == 1 or j == height:
                print(outline,end = "")
            else:
                print(fill,end = "")
        else:
            print(" ",end = "")
    print()
    w+=2