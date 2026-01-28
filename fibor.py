#by recursion
def fibo(n): 
    if(n<=0):
        print("invalid output")
    elif(n==1):  
        return [0]
    elif (n==2):
        return[0,1]
    else:
        seq = fibo(n-1)   
        seq.append(seq[-1] + seq[-2])  
        return seq
n=int(input("enter the no. of terms"))
f=fibo(n)
print(f)