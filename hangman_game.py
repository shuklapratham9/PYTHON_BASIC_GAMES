import random as r
def hang(a):
    if a==0:
        print('''          +--------+
          O     |
                |
                |
                |  ''')
    if a==1:
        print('''          +--------+
          O     |
         /      |
                |
                |  ''')
    if a==2:
        print('''          +--------+
          O     |
         / \    |
                |
                |  ''')
    if a==3:
        print('''          +--------+
          O     |
         /|\    |
                |
                |  ''')
    if a==4:
        print('''          +--------+
          O     |
         /|\    |
         /      |
                |  ''')
    if a==5:
        print('''          +--------+
          O     |
         /|\    |
         / \    |
                |  ''')
print('Welcome to the Bollywood Hangman Game'.center(120))
s=['major','super30','genius','kesari','dhrishyam','race','players','faltu','raone','krish','dhol','jigar','sultan','sanju','rustom']
print('''Instructions: 
You have to guess a bollywood movie name according to the spaces and hints.
In all you have 5 chances.
At every incorrect guess hangman will start to form and when it is complete the game is over and you lose.''')
ch=input("READY TO PLAY THE GAME\nEnter Yes or No : ").capitalize()
def hangmangame():
    if ch=="Yes":
        a=r.choice(s)
        m=r.randint(0,len(a))
        n=r.randint(0,len(a))
        k=[]
        for i in range (len(a)):
            if i==m:
                print(a[i],end='')
                k.append(a[i])
            elif i==n:
                print(a[i],end='')
                k.append(a[i])
            else:
                print("_",end='')
                k.append("_")
        print()
        ms=[]
        c=0
        while True:
            b=input("Enter the missing alphabet : ").lower()
            if b in a:
                ct=0
                for i in range (len(a)):
                    if b==a[i]:
                        ct=i
                k[ct]=a[ct]
                for j in k:
                    print(j,end=' ')
                print()
                hang(c)
                if k==list(a):
                    print("Yeah! Its a win".center(50))
                    break
            else:
                c=c+1
                ms.append(b)
                print("Missed letters : ",ms)
                for j in k:
                    print(j,end=' ')
                print()
                hang(c)
                if c==5:
                    print("Correct answer is : ",a.capitalize(),"\nGame Over".center(50))
                    break
                if k==list(a):
                    print("Yeah! Its a win".center(50))
                    break
    rec=input("Do you want to play again ( Yes or No ) : ").capitalize()
    if rec=="Yes":
        hangmangame()
hangmangame()
