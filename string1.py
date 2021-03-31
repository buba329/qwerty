str1=input('Write string: ')
str2=''
flag=True
for i in range(len(str1)-1,-1,-1):
    str2+=str1[i]
for i in range(len(str1)):
    if str2[i]!=str1[i]:
        flag=False
        break
if flag:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")