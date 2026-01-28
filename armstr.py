count=0
q=input("enter the number u want to check")
l=len(q)
for i in range(0,l):
    count=count+(int(q[i])**l)
if(int(q)==count):
    print("no. is armstrong")
else:
    print("no. is not armstrong")