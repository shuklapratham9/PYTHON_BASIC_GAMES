import random
st='                 **********WELCOME TO GUESS THE NUMBER GAME**********'
e='''RULES :
    1.COMPUTER WILL SELECT A NUMBER RANDOMLY FROM A GIVEN RANGE
    2.ACCORDING TO YOUR CHOOSEN LEVEL TO HAVE GUESS THE NUMBER IN MINIMUM POSSIBLE ATTEMPTS'''
print(st.title())
print(e)
print('CHOOSE THE LEVEL')
print('(1)EASY','(2)MEDIUM','(3)PRO',sep='\n')
lvl=int(input('Enter the level: '))
if lvl==1:
    print('YOU HAVE TO GUESS A NUMBER BETWEEN 1 T0 100','YOU HAVE UNLIMITED ATTEMPTS')
    n=random.randint(1,100)
    g=0
    c=0
    while n!=g:
        g=int(input('Enter your guess precisely: '))
        c+=1
        if g==n:
            print("YOU WON IN",c,"MOVES")
            print("COMPUTER SELECTED",n)
            break
elif lvl==2:
    print("YOU HAVE TO GUESS A NUMBER BETWEEN 1 TO 100",'YOU HAVE ONLY 20 ATTEMPTS',sep='\n')
    n=random.randint(1,50)
    g=0
    att=20
    t=att
    while att>0:
        g=int(input("Enter your guess precisely: "))
        att-=1
        if g==n:
            print("YOU WON IN",t-att,"MOVES")
            break
        elif g<n:
            print("GUESS IS SMALL")
            print(att,"ATTEMPTS LEFT")
        else:
            print("GUESS IS LARGE")
            print(att,"ATTEMPTS LEFT")
    else:
        print("YOU DIDN'T GUESS IT","BETTER LUCK NEXT TIME",sep='\n')
        print("COMPUTER SELECTED",n)
elif lvl==3:
    print("YOU HAVE TO GUESS A BETWEEN FROM 1 TO 20",'YOU HAVE ONLY 5 ATTEMPTS',sep='\n')
    n=random.randint(1,20)
    g=50
    att=5
    t=att
    while att>0:
        g=int(input("Enter your guess precisely: "))
        att-=1
        if g==n:
            print("YOU WON IN",t-att,'MOVES')
            print("COMPUTER SELECTED",n)
            break
        elif g<n:
            print('GUESS IS SMALL')
            print(att,'ATTEMPTS LEFT')
        else:
            print('GUESS IS LARGE')
            print(att,'ATTEMPTS LEFT')
    else:
        print("YOU DID'T GUESSED IT",'BETTER LUCK NEXT TIME')
        print("COMPUTER SELECTED",n)
            
else:
    print("INVALID INPUT")
