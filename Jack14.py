# Program to check Armstrong number

num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + (digit ** 3)
    num = num // 10

if original == sum:
    print(original, "is an Armstrong number.")
else:
    print(original, "is not an Armstrong number.")
