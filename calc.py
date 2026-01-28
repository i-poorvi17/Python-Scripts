try:
        import math
        def sum(a,b):
            return a+b
        def sub(a,b):
            return a-b
        def multi(a,b):
            return a*b
        def div(a,b):
            return a/b
        def log(a):
            return math.log10(a)
        def pow(a,b):
            return math.pow(a,b)
        def per(a,b):
            return a*(b/100)
        a=float(input("enter the number\n"))
        
        while True:
            s = input("Enter operation (+ - * / % ^ log) or # to exit: ")
            if(s=='%'):
                b=float(input("enter the percent\t"))        
                a=per(a,b)
            elif(s=='#'):
                break
            elif s in ['+', '-', '*', '/','^']:
                    b=float(input("enter the 2nd operand\t"))
                    if(s=='+'):
                       a=sum(a,b)
                    elif(s=='-'):
                        a=sub(a,b)
                    elif(s=='*'):
                        a=multi(a,b)
                    elif(s=='/'):
                        a=div(a,b)
                    elif(s=="^"):
                        b=float(input('enter the power'))
                        a=pow(a,b)
                    elif(s=='log'):
                        a=log(a)
            else:
                    print("invalid operator")
            print(a) 
                 
except Exception as e:
    print("error occured", e)
finally:
    print('calculation  ended')
            