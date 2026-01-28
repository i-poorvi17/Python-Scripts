score=0
while True:
    print("let's play snake water gun game")
    import random
    computer=['snake','water','gun']
    computer=random.choice(computer)
    user=int(input("choose \n 1. snake \n 2. water \n 3.gun \n 4. dont want to play more exit\n"))
    if(computer=='snake'):
        if (user ==1):
            print(f'computer choose {computer}')
            print(f'tie! try again, ur score is {score}\n')
        elif(user==3):
            print(f'computer choose {computer}')
            print("u win! u shoot it downn\n")
            score=score+1
            print(f"ur score is {score}\n")
        elif(user==2):
            print(f'computer choose {computer}')
            print(f"aww! u lose, ur score is {score}\n")
    elif(computer=='water'):
        if (user==1):
            print(f'computer choose {computer}')
            score=score+1
            print(f'you win! u drink the water so fast \n ur score is {score}\n')
        elif(user==3):
            print(f'computer choose {computer}')
            print(f"u lose! u gun sink {score}\n")
        elif(user==2):
            print(f'computer choose {computer}')
            print(f"tie! ur score is {score}\n")
    elif(computer=='gun'):
        if (user==1):
            print(f'computer choose {computer}')
            print(f'u lose ur score is {score}\n')
        elif(user==3):
            print(f'computer choose {computer}')
            print(f"tie! ur score is {score}\n")
        elif(user==2):
            print(f'computer choose {computer}')
            score=score+1
            print(f"you win it ! ur score is {score}\n")   
    else:
        break
     

