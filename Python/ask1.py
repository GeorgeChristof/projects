k=int(input('Dwse k: '))
l=int(input('Dwse l: '))
m=int(input('Dwse m: '))
n=int(input('Dwse n: '))
mo=(k+l+m+n)/4
print('O mesos oros einai: ',mo)
max=k
min=k

if(max<l):
    max=l
if(max<m):
    max=m
if(max<n):
    max=n

if(min>l):
    min=l
if(min>m):
    min=m
if(min>n):
    min=n
print('Megaluteros: ',max)
print('Mikroteros: ',min)

sum=k+l+m+n
gin=k*l*m*n

if(sum%2==0):
    print('Athroisma %d ,Artios' %sum)
else:
    print('Athroisma %d ,Perittos'%sum)

if(gin%2==0):
    print('Ginomeno %d ,Artios'%gin)
else:
    print('Ginomeno %d ,Perittos'%gin)

suma1=0
if(k>10):
    suma1+=1
if(l>10):
    suma1+=1
if(m>10):
    suma1+=1
if(n>10):
    suma1+=1
print('Megalyteroi tou 10: ',suma1)
