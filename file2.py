a=['name','surname','age','class']
f=open("studentslist.py","r")
r=f.read()
if r=='':
    f=open("studentslist.py","w")
    f.write("   "+a[0]+"        "+a[1]+"     "+a[2]+"         "+a[3]+"\n")
    f.close()
f.close()
z=-1
x=0
if r!='':
    count=len(r.split('\n'))-2
else:
    count=0
while z!=0:
    z=int(input('0 - Закончить работу со списком\n1 - Внести ученика(ов) в список\n2 - Вывести весь список учеников\n3 - Найти ученика(ов)\nВыбор: '))
    if z==1:
        f=open("studentslist.py","a")
        x=int(input('How many students? '))
        for count in range(count+1,count+x+1):
            if count>9:
                f.write(str(count)+" ")
            else:
                f.write(str(count)+"  ")
            for q in range(4):
                n=input(f"Student's {a[q]}: ")
                x1=12-len(n)
                if q<3:
                    f.write(n)
                    for i in range(x1):
                        f.write(" ")
                else:
                    f.write(n+"\n")
        f.close()
    if z==2:
        f=open("studentslist.py","r")
        r=f.read().split("\n")
        f.close()
        for i in range(len(r)-1):
            print(r[i])
    if z==3:
        f=open("studentslist.py","r")
        data = f.readlines()
        data.pop(0)
        r=" ".join(data).split()
        f.close()
        print(r)
        kr=int(input("Search student by:\n1 - name\n2 - surname\n3 - age\n4 - class\nChoice: "))
        search=input(f"Choose the {a[kr]}: ")
        for i in range(kr,len(r),5):
            if r[i]==search:
                for q in range(i-kr+1,i-kr+5):
                    print(r[q],end=" ")
                print()
print("Работа со списком закончена. Хорошего дня, пользователь!")