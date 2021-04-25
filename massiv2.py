import random
a=[]
adop=[]
X=int(input('Сколько эелементов должно быть в массиве? '))
x1=int(input('Сколько элементов должно быть во внутренних массивах? '))
s=0
mx=100
mn=9
for i in range(X):
    adop=[]
    for q in range(x1):
        n=random.randint(10,99)
        s+=n
        adop.append(n)
    for q in range(x1):
        if adop[q]>mn:
            mn=adop[q]
        if adop[q]<mx:
            mx=adop[q]
    adop.append(s)
    adop.append(mn)
    adop.append(mx)
    a.append(adop)
    s=0
    mn=9
    mx=99
for i in range(X):
    for q in range(x1+3):
        print(a[i][q],end='\t')
        if q==x1-1:
            print('|',end='\t')
    print()