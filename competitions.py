import random
X=int(input('Количество команд: '))+1
x1=int(input('Сколько было игр? '))+1
a=[]
adop=['']
name=''
s=0
mx=5*(X-1)
for i in range(1,x1):
    adop.append(f'{i} game:')
a.append(adop)
for i in range(1,X):
    name=input('Введите название команды: ')
    adop=[f'{name}']
    for q in range(x1):
        n=random.randint(1,5)
        adop.append(n)
    a.append(adop)
for i in range(x1):
    for q in range(X):
        print(a[q][i],end='\t')
    print()
for i in range(1,X):
    for q in range(1,x1):
        s+=a[i][q]
    if s<mx:
        mx=s
        name=a[i][0]
print(f'Победитель - "{name}"!')