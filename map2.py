students=[]
x=int(input('How many students? '))
a=['name','surname','age','class']
for i in range(x):
    student={}
    for q in range(4):
        n=input(f"Student's {a[q]}: ")
        student[a[q]]=n
    students.append(student)
for i in students:
    for key in i:
        print(i[key],end=" ")
    print()
kr=int(input("Search student by:\n1 - name\n2 - surname\n3 - age\n4 - class\nChoice: "))-1
kr=a[kr]
search=input(f"Choose the {kr}: ")
for i in students:
    if i[kr]==search:
        for key in i:
            print(i[key],end=" ")
        print()