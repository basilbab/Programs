a=int(input())
while(a==0):
    if(a<0):
        a=-1
    if(a>0):
        a=1
    print('infinite loop')
if(a>1):
    a=2
if(a<1):
    a=-2
print(a)    
