count = 0
while count<3:
    print('Parolu daxil edin: ')
    a=input()
    if(len(a)>=8 and len(a)<=13):
        print('Kechdiniz')
    else:
            print('yanlish parol!')
            count+=1
print("Yeniden yoxlayin")