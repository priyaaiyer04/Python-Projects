import random
print("Try programiz.pro")
print("enter 2 numbers")
a=int(input())
b=int(input())
c=random.randint(a, b)
print("guess the random number")
d=int(input())
if d==c:
        print("correct guess")
else:
    while d!=c:
        if d>c:
            print("guessed high, try again")
        if d<c:
            print("guessed low, try again")
        d=int(input())
        if d==c:
            print("correct guess")