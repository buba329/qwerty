a=1
x=1
while a!=0:
    a=int(input("Введите число: "))
    if a==0:
        break
    x*=a
print(x)