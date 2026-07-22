num = int(input("Enter a number: "))

sqr = num * num

if str(sqr).endswith(str(num)):
    print("It is an Automorphic Number")
else:
    print("Not an Automorphic Number")
