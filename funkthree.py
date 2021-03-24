def dvatreugol(n):
    for i in range(0,n):
        for i in range(5,0,-2):
            for b in range((5-i)//2,0,-1):
                print(" ",end="")
            for q in range(0,i):
                print("*",end="")
            print()
        for i in range(3,5+1,2):
            for b in range((5-i)//2,0,-1):
                print(" ",end="")
            for q in range(0,i):
                print("*",end="")
            print()
dvatreugol(3)