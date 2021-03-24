import random
arr=[]
def search(arr,n):
    res=[]
    for i in range(len(arr)):
        if arr[i]==n:
            res.append(i)
    return res
x=int(input("Сколько элементов должно быть в массиве? "))
for i in range(x+1):
    a=random. randint(1,100)
    arr.append(a)
def print_arr(arr)
    for i in range(x):
        if i==x-1:
            print(arr[i],end=".\n")
        else:
            print(arr[i],end=", ")
n=int(input("Какое число (от 1 до 100) из массива вы желаете получить? "))
if len(search(arr,n))==0:
    print("Элемента, содержащего такое число, не существует")
else:
    print("Элемент(ы)",search(arr,n),"Содержит это число")