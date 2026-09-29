age = int(input("Вік людини: "))

if age % 100 >= 11 and age % 100 <= 14:
    print(age,"років")
else:
    if age % 10 == 1:
        print(age,"рік")
    elif age % 10 >= 2 and age % 10 <= 4:
        print(age,"роки")
    else:
        print(age,"років")