a=int(input("Введите номер билета: "))
while a>999999 or a<100000:
    a=int(input("Введите номер билета: "))
x1=0
x2=0
while a>999:
    x1+=a%10
    a=a//10
while a!=0:
    x2+=a%10
    a=a//10
if x1==x2:
    print("Билет счастливый!")
else:
    print("Билет не счастливый :(")