import random
l=[chr(i) for i in range(65,91)]
for i in range(97,123):
    l.append(chr(i))
for i in range(1,10):
    l.append(str(i))
for i in range(33,39):
    l.append(chr(i))
n=int(input("Enter the length of your password: "))
v=''
for i in range(len(l)):
    v=v+random.choice(l)
print(v[-1:-n-1:-1])
