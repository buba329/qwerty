import random
import deff
x = int(input("Сколько оценок? "))
arr=[]
flag=False
a=0
for i in range(x):
    arr.append(random.randint(2,5))
    if arr[i]==2:
        flag=True
deff.print_arr(arr)
if flag:
    print("Ученик двоечник")
else:
    for i in range(x):
        a+=arr[i]
        if a==5*x:
            flag=True
    if flag:
        print("Ученик отличник")