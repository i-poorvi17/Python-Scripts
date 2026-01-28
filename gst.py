while True:
    print( '\n' )
    cop=float(input("enter the cost of product"))
    x=int(input("categories defined for gst \n\n 1.essentials(milk,eggs,fresh vegetables),healthcare,hopstialsand educational services \n\n 2. packaged food,transport,household essentials ,small vehicles,\n\n  3. Mobile Phones,processed foodS, all mostly goods and services , electronics and restaurants \n\n 4. luxury goods,tobacco products, expensive cars\t"))
    total=0
    if(x==1):
        print('total cost=',cop)
    elif(x==2):
        total=cop+(0.05*cop)
        print('cgst= 2.5% \n sgst=2.5% \n total cost=',total,'/-only')
    elif(x==3):
        total=cop+(0.18*cop)
        print('cgst= 9.0% \n sgst=9.0% \n total cost=',total,'/-only')
    elif(x==4):
        total=cop+(0.40*cop)
        print('cgst= 20.0% \n sgst=20.0% \n total cost=',total,'/-only')
    else:
        print('invalid input')
        break