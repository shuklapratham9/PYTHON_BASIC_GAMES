import random
print("***************""WELCOME TO THE GAME OF ROCK PAPER'S AND SCISSOR""*****************")
j=["SCISSOR","ROCK","PAPER"]
c=random.choice(j)
m=[1,2,3]
print("CHOOSE YOUR OPTION")
print("1. Enter 1 for SCISSOR","2. Enter 2 for ROCK","3. Enter 3 for PAPER",sep='\n')
while True:
    g=int(input("Enter your choice precisely: "))
    if g not in m:
        print("INVALID INPUT")
        break
    elif (g==1 and c==j[2])or(g==2 and c==j[0])or(g==3 and c==j[1]):
        print("CONGRATULATIONS YOU WON")
        print("COMPUTER SELECTED",c)
    elif (g==1 and c==j[0])or(g==2 and c==j[1])or(g==3 and c==j[2]):
        print('MATCH TIED')
        print("YOU AND COMPUTER BOTH SELECTED",c)
    else:
        print("YOU DUMB BOY YOU LOST")
        print("COMPUTER SELECTED",c)
    u=input("Enter 'y' if you want to play again or 'n' if you don't want to play again: ")
    if u=='y'or u=='Y':
        continue
    else:
        break
   
    

