while True:
    terms=int(input("enter the no. of terms u want in series"))
    n1=0
    n2=1
    count=0
    if(terms==0):
        print("enter a positive value")
        break
    if(terms==1):
        print("series will be ",n1)
        break
    print(n1)
    print(n2)
    for i in range(0,terms-2):
        count=n1+n2
        n1=n2
        n2=count
        print(count)
    x=input('do u want to continue say yes/no')
    if(x=='no'):
        break

