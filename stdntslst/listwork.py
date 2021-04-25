import json
import os.path
def print_students(arr,key,sub,i):
    for key in students[i]:
        while key!=marks:
            print(arr[i][key],end=" ")
        for sub in arr[i][key]:
            print(sub,arr[i][key][sub],end=" ")
a=["name","searname","patronymic","group","marks"]
print("Здравствуй пользователь!")
if os.path.exists("list.json"):
    f=open("list.json","r")
    students=json.load(f)
else:
    students=[]
z=-1
while z!=8:
    z=int(input("Выберите действие:\nВывести список учеников - 1\nВывести учеников по номеру группы - 2\nДобавить данные о студенте в список - 3\nУдалить данные о студенте из списка - 4\nИзменить данные о студенте - 5\nВывести отличников - 6\nВывести двоечников - 7\nЗавершить работу - 8\nВыбор: "))
    if z==1:
        for i in students:
            print_students(students,key,sub,i)
            print()
    if z==2:
        searchgroup=input("Введите название группы")
        for i in students:
            if searchgroup in students[i][group]:
                print_students(students,key,sub,i)
                print()
    if z==3:
        sub=int(input("Сколько предметов у студента"))*2+4
    if z==4:
    if z==5:
    if z==6:
    if z==7:
print("Работа со списком закончена. Хорошего дня, пользователь!")