a=int(input("Введите число: "))
for i in range(1,a+1):
    for q in range(1,a+1):
        if i==q:
            print("*",end="")
        elif q-1==a-i:
            print("*",end="")
        else:
            print(end=" ")
    print()