import random
import deff
arr=[]
flag=True
for i in range(30):
    arr.append(random.randint(-5,5))
deff.print_arr(arr)
for i in range(len(arr)):
    if arr[i]<0:
        flag=False
if flag==False:
    print("Месяц холодный")