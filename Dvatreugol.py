a=int(input("Введите первое число: "))
for i in range(a,0,-2):
    for b in range((a-i)//2,0,-1):
        print(" ",end="")
    for q in range(0,i):
        print("*",end="")
    print()
for i in range(3,a+1,2):
    for b in range((a-i)//2,0,-1):
        print(" ",end="")
    for q in range(0,i):
        print("*",end="")
    print()
