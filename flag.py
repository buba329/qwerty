import random
import deff
x = int(input("Сколько оценок? "))
arr=[]
flag=True
for i in range(x):
    arr.append(random.randint(2,5))
    if arr[i]==2:
        flag=False
deff.print_arr(arr)
if flag==False:
    print("Ученик двоечник")
else:
    for i in range(x):
        if arr[i]!=5:
            flag=False
    if flag:
        print("Ученик отличник")