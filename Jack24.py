import math

num=int(input("Enter a number:"))
a=int(math.sqrt(num))

if a*a==num:
    print("It is a perfect square")
else:
    print("It is not perfect number")
