a=int(input("Введите число от единицы до ста миллионов: "))
ed=['','one','two','three','four','five','six','seven','eight','nine']
ttn=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
spec=['hundred','thousand','million']
strdop=''
str0=''
def string(strn,arr1,arr2,arr3,arr4,chislo):
    if chislo//100>0:
        strn+=arr1[chislo//100]+' '+arr4[0]+' '
    chislo%=100
    if chislo//10==1:
        if chislo%10>0:
            strn+=arr2[chislo%10]
        else:
            strn+=arr2[0]
    else:
        strn+=arr3[chislo//10]+' '
        strn+=arr1[chislo%10]
    return strn
if a>999999:
    str0+=string(strdop,ed,ttn,tens,spec,a//1000000)+' '+spec[2]+' '+string(strdop,ed,ttn,tens,spec,(a//1000)%1000)+' '+spec[1]+' '+string(strdop,ed,ttn,tens,spec,a%1000)
elif a>999:
    str0+=string(strdop,ed,ttn,tens,spec,a//1000)+' '+spec[1]+' '+string(strdop,ed,ttn,tens,spec,a%1000)
else:
    str0+=string(strdop,ed,ttn,tens,spec,a)
print(str0)