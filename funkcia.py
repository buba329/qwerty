m=int(input("Введите первое число: "))
n=int(input("Введите второе число: "))
def fact(a):
    a1=1
    for i in range(1,a+1):
        a1*=i
    return a1
if m>n:
    print(fact(m)/fact(n)/fact(m-n))
elif n>m:
    print(fact(n)/fact(m)/fact(n-m))
else:
    print("Действие невозможно")
a=int(input("Какое число вы хотите получить? "))
def feb(a):
    x1=0
    x2=1
    x3=0
    for i in range (1,a):
        x3=x1+x2
        x1=x2
        x2=x3
    return x3
print(feb(a))