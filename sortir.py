import random
import deff
arr=[]
x=int(input("Сколько элементов должно быть в массиве? "))
for i in range(x):
    arr.append(random.randint(-100,100))
deff.print_arr(arr)
for i in range(x):
    for i in range(x-1):
        if arr[i]>arr[i+1]:
            dop=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=dop
deff.print_arr(arr)
n=int(input("Какое число ноужно найти? "))
for i in range(x):
    if arr[(x-1+i)//2]>n:
        x=(x-1+i)//2-1
    elif arr[(x-1+i)//2]<n:
        i=(x-1+i)//2+1
    else:
        print("Элемент arr[",(x-1+i)//2,"] Содержит это число")
        break