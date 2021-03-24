n=int(input("Введите длину стороны квадрата: "))
def print_line(n):
    for i in range(0,n):
        print("*",end="")
for q in range(0,n):
    print_line(n)
    print()