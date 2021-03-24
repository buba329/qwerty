import math
a=int(input("Введите коэффицент: a "))
b=int(input("Введите коэффицент: b "))
c=int(input("Введите коэффицент: c "))
print(f"Уравнение: {a}x*x+({b}x)+({c})=0")
D=b*b-4*a*c
if D>0:
    print("Уравнение имеет 2 корня")
    print(f"x={(-1)*b+math.sqrt(D)/2/a} ; {(-1)*b-math.sqrt(D)/2/a}")
elif D==0:
    print("Уравнение имеет 1 корень")
    print(f"x={(-1)*b/2/a}")
else:
    print("Уравнение не имеет корней")
