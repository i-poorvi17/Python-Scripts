import time
def greet():
    
    timestamp=time.strftime('%H')
    c=int(timestamp)
    if(c<12):
        print("good morning")
    elif(c<16):
        print("good afternoon")
    elif(c<20):
        print("good evening")
    elif(c<24):
        print("good night")
greet()

