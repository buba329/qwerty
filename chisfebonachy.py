a=int(input("Введите номер числа из ряда Фебоначи: "))
x1=0
x2=1
x3=0
for i in range (1,a):
    x3=x1+x2
    x1=x2
    x2=x3
print(x3)