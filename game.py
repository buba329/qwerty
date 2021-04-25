f=open("gamelist","r")
r=f.readlines()
r=" ".join(r).split()
f.close()
players = {}
for i in range(0,len(r),2):
    players[r[i]] = int(r[i+1])
player1=input('Введите имя игрока 1: ')
if player1 not in players:
    players[player1] = 0
player2=input('Введите имя игрока 2: ')
if player2 not in players:
    players[player2] = 0
a=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
x=0
y=0
def draw_field(arr):
    for i in range(3):
        if i<2:
            for q in range(3):
                if q<2:
                    print(arr[i][q],end='|')
                else:
                    print(arr[i][q])
            print('-+-+-')
        else:
            for q in range(3):
                if q<2:
                    print(arr[i][q],end='|')
                else:
                    print(arr[i][q])
def turn(arr,strok,stolb,count):
    strok=int(input('Выберите строку: '))-1
    stolb=int(input('Выберите столбец: '))-1
    while arr[strok][stolb]!=' ':
        print('Эта ячейка занята!')
        strok=int(input('Выберите строку: '))-1
        stolb=int(input('Выберите столбец: '))-1
    if count%2==0:
        arr[strok][stolb]='X'
    else:
        arr[strok][stolb]='O'
    return arr
def check_win(arr,count):
    for i in range(3):
        if (arr[0][i]==arr[1][i] and arr[0][i]==a[2][i] and arr[0][i]!=' ') or (arr[i][0]==arr[i][1] and arr[i][0]==arr[i][2] and arr[i][0]!=' '):
            return True
    if (arr[0][0]==arr[1][1] and arr[0][0]==arr[2][2] and arr[0][0]!=' ') or (arr[0][2]==arr[1][1] and arr[0][2]==arr[2][0] and arr[0][2]!=' '):
        return True
    return False
for q in range(9):
    if q%2==0:
        print(f'Ходит {player1}')
    else:
        print(f'Ходит {player2}')
    draw_field(turn(a,x,y,q))
    if check_win(a,q) and q%2==0:
        print(f'Выиграл {player1}')
        players[player1]+=1
        break
    elif check_win(a,q) and q%2==1:
        print(f'Выиграл {player2}')
        players[player2]+=1
        break
    elif q==9:
        print("Ничья")
f=open("gamelist","w")
for key in players:
    f.write(f"{key} {players[key]}\n")
f.close()