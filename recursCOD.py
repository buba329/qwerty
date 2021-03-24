k=1
def cod(a,k):
    if a==0:
        return 0
    elif a//k==9:
        print(1,end="")
        return cod(a%k,k//10)
    else:
        print(a//k+1,end="")
        return cod(a%k,k//10)
a=int(input("Введите трёхзначное число: "))
x=a//10
while x>0:
    x//=10
    k*=10
if k==1:
    print('0 нельзя')
else:
    cod(a,k)
print()