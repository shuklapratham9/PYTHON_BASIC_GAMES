import random
s=str(random.random())
n=int(input("Enter the number of digits you want in your O.T.P: "))  #ENTER THE NUMBER OF DIGITS IN THE O.T.P
print(s[-1:-1*(n+1):-1])

