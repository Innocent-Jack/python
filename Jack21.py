num = int(input("Enter a number: "))

i = 2

while num > 1:
    if num % i == 0:
        num = num // i
        print(i)
    else:
        i = i + 1
