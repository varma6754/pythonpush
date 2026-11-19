'''to generate a random number and i have to find the number only 5 attempts'''
import random
b=random.randint(1, 100)

for i in range(5) :
    a=int(input("enter the input"))
    if a>b:
        print("high")
    elif a<b:
        print("low")
    else:
        print("Correct! You won")
        break
    
else:
    print("you lost the number is",b )
