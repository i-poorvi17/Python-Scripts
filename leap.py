y=int(input("enter the year"))
if(y%4==0 and y%400==0):
        print('year is leap year')
elif (y%100!=0):
    print("year is leap")
else:
      print("year is not leap")
