a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
a1=1
b1=1
ab=1
for i in range(1,a+1):
    a1*=i
for i in range(1,b+1):
    b1*=i
if a>b:
    for i in range(1,a-b+1):
        ab=i
    print(a1/b1/ab)
elif b>a:
    for i in range(1,b-a+1):
        ab=i
    print(b1/a1/ab)
else:
    print("Действие невозможно")