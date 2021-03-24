a=int(input("Введите число: "))
x=1
print(f"Факторисал числа {a} равен: ",end="")
while a!=0:
    x*=a
    a-=1
print(x)