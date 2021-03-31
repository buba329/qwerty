str1=input('Напишите строку: ')
i=0
x=len(str1)-1
flag=True
while i<=x:
    if str1[i]==' ':
        i+=1
    if str1[x]==' ':
        x-=1
    elif str1[i]!=str1[x]:
        flag=False
        break
    else:
        x-=1
        i+=1
if flag:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")