def print_arr(a):
    for i in range(len(a)):
        if i==len(a)-1:
            print(a[i],end=".\n")
        else:
            print(a[i],end=", ")