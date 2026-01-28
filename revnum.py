rev=0
x=int(input("enter the number u want to reverse"))
while x>0:
    rev= (rev*10)+(x%10)
    x= x//10
print(rev)
