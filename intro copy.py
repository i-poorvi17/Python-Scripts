class programmer:
    company='microsoft'
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode
        print(f'my name is {self.name} and the salary {self.salary} and belongs to {self.pincode} and from {self.company}')
        
name=input("enter the name")
salary=input("enter the salary")
pincode=input("enter the place pincode")
p=programmer(name,salary,pincode)


        