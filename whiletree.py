a=int(input("Введите чило: "))
x=1
while a!=0:
    x+=a%10
    a=a//10
print(x)