import random
a=[]
adop=[]
X=int(input('Сколько эелементов должно быть в массиве? '))
x1=int(input('Сколько элементов должно быть во внутренних массивах? '))
str0=''
for i in range(X):
    adop=[]
    for q in range(x1):
        n=random.randint(-100,100)
        adop.append(n)
    a.append(adop)
for i in range(x1):
    for q in range(X):
        if a[q][i]>=0:
            print(end=' ')
        print(a[q][i],end='\t')
    print()
n=int(input('Какое число вам нужно? '))
for i in range(X):
    for q in range(x1):
        if a[i][q]==n:
            str0+=f'{i}-го '
print(f'Заданное число находится внутри {str0}внутреннего(их) массива(ов)')