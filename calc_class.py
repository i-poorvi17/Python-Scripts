import math
class calculator:
    def __init__(self,x):
        self.square=x*x
        self.cube=x*x*x
        self.root=math.sqrt(x)
x=int(input("enter the number"))
p= calculator(x)
print(p.square,p.cube,p.root)
        