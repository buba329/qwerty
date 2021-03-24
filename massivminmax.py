import random
import deff
arr=[]
mx=0
mn=0
x=int(input("Сколько элементов должно быть в массиве? "))
for i in range(x):
    arr.append(random.randint(-100,100))
deff.print_arr(arr)
for i in range(len(arr)):
    if arr[i]>arr[mx] and arr[i]%2==0:
        mx=i
    if arr[i]<arr[mn]:
        mn=i
if arr[mx]%2!=0:
    print("Чётных нет")
else:
    print(f"Максимальный чётный элемент: А[{mx}] = {arr[mx]}")