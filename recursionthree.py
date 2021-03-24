def summacifr(a):
    if a>=0 and a<10:
        return a
    elif a>=10:
        return a%10+summacifr(a//10)
a=int(input("Введите число"))
print(summacifr(a))