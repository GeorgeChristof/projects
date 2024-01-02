car=input('marka: ')
while(car!= 'end') and (car!= 'END'):
    cc=int(input('cc: '))
    if(cc<=1000):
        tax=120
    elif(cc<=1370):
        tax=135
    elif(cc<=2000):
        tax=280
    elif(cc<=3000):
        tax=820
    else:
        tax=1230
    print('Car %s, cc: %d, Tax: %d' %(car,cc,tax))
    car=input('marka: ')
