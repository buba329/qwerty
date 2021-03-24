def naoborot(a):
    if a>=0 and a<10:
        print (a,end="")
    elif a>=10:
        print(a%10,end="")
        return naoborot(a//10)
a=int(input("Введите чсло: "))
naoborot(a)
print()