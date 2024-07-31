name=input('Enter your name')
age=int(input('Enter your age'))
flag="False"
if(age>=18):
    flag="True"
else:
    flag="False"
counter=0
for i in name:
    if(i=='a'):
        counter+=1
if(flag=='True'):
    if(counter>2):
        print('You are lucky')
    else:
         print('You are not lucky')