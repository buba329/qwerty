a=int(input("Ширина: "))
h=int(input("Высота: "))
x=int(input("Абсцисса центра: "))
y=int(input("Оордината центра: "))
x1=int(input("Абсцисса точки: "))
y1=int(input("Оордината точки: "))
xmax=x+a/2
ymax=y+h/2
xmin=x-a/2
ymin=y-h/2
if (x1>xmin or x1==xmin) and (x1<xmax or x1==xmax) and (y1>ymin or y1==ymin) and (y1<ymax or y1==ymax):
    print(f"Точка ({x1};{y1}) входит в прямоугольник")
else:
    print(f"Точка ({x1};{y1}) не входит в прямоугольник")