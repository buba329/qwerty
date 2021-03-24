a=int(input("Введите первое число: "))
for i in range(1,a+1):
    for b in range(a-i,0,-1):
        print(" ",end="")
    for q in range(0,i):
        print("*",end="")
    print()
a=int(input("Введите первое число: "))
for i in range(a,0,-1):
    for b in range(a-i,0,-1):
        print(" ",end="")
    for q in range(0,i):
        print("*",end="")
    print()