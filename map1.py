import random
x=int(input('Количество команд: '))
x1=int(input('Сколько было игр? '))
a={}
adop=[]
key=''
s=0
for i in range(x):
    key=input('Введите название команды: ')
    a[key]=[]
    for q in range(x1):
        n=random.randint(1,5)
        adop.append(n)
    a[key]=adop
    adop=[]
for key in a:
    print(key,end='\t')
    for i in a[key]:
        print(i,end='\t')
    print()