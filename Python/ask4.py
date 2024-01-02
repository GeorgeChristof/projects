print('1.add')
print('2.substract')
print('3.multiply')
print('4.divide')
print('5.end')
x=int(input('select: '))
while(x!=5):
    if(x>=0) and (x<5):
        a=int(input('a: '))
        b=int(input('b: '))
        if(x==1):
            k=a+b
        elif(x==2):
            k=a-b
        elif(x==3):
            k=a*b
        elif(x==4):
            k=a/b
        print('result: ',k)
    
    print('1.add')
    print('2.substract')
    print('3.multiply')
    print('4.divide')
    print('5.end')
    x=int(input('select: '))
