import random
a=[]
adop=['','NAVI','GAMBIT','TeamONE','Virtus','Astral']
X=6
x1=int(input('Сколько было игр? '))+1
str0=''
count=-1
s=0
for i in range(X):
    count+=1
    if i>0:
        adop=[f'{count}-я']
    for q in range(x1):
        n=random.randint(1,5)
        adop.append(n)
    a.append(adop)
for i in range(x1):
    for q in range(X):
        print(a[q][i],end='\t')
    print()
for i in range()