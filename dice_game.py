import random
'''HERE COMPUTER WILL RANDOMLY SELECT NUMBER BETWEEN 1 TO 6 AND WILL PRINT
THE FACE OF THE DICE REPRESENTING THAT NUMBER'''
l=[1,2,3,4,5,6]

a=random.choice(l)
print("COMPUTER SELECTED",a)
if a==1:
    print(' _____\n|     |\n|  o  |\n|     |\n|_____|')
elif a==2:
    print(' _____\n|     |\n| o o |\n|     |\n|_____|')
elif a==3:
    print(' _____\n|     |\n| o o |\n|  o  |\n|_____|')
elif a==4:
    print(' _____\n|     |\n| o o |\n| o o |\n|_____|')
elif a==5:
    print(' _____\n| o o |\n|  o  |\n| o o |\n|_____|')
elif a==6:
    print(' _____\n| o o |\n| o o |\n| o o |\n|_____|')
