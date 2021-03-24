a=int(input("Введите число: "))
for i in range(1,a+1):
    for q in range(1,a+1):
        if (q==i or q>i) and q>a-i:
            print("*",end="")
        else:
            print(end=" ")
    print()