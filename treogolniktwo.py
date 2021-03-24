a=2
while a%2==0:
    a=int(input("Введите число: "))
for i in range(1,a+1):
    for q in range(1,a+1):
        if (q>=i and q>a-i) or (q<=i and q-1<=a-i):
            print("*",end="")
        else:
            print(end=" ")
    print()