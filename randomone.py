import random
a=random. randint(1,100)
print("Угадай число от одного до ста!")
x=0
n=0
while x!=a:
    x=int(input("Введи число: "))
    n+=1
    if x<a:
        print("Ваше число меньше")
    elif x>a:
        print("Ваше число больше")
    else:
        print(f"Правильно! Вы использовали {n} попыток.")