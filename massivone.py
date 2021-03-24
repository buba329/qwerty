arr=[]
x=int(input("Сколько элеиентов должно быть в массиве? "))
for i in range(x):
    a=int(input(f"Введите {i}-й элемент "))
    arr.append(a)
for i in range(x):
    if i==x-1:
        print(arr[i],end=".\n")
    else:
        print(arr[i],end=", ")