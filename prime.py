x=int(input("enter the number u want to check"))
p=0
for i in range(2,x):
    if(x%i==0):
        p=p+1
        break
if(p==0):
    print('prime')
else:
    print('not prime')