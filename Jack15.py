# Armstrong numbers in a given range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong numbers are:")

for num in range(start, end + 1):
    original = num
    sum = 0
    power = len(str(num))
    temp = num

    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** power)
        temp = temp // 10

    if original == sum:
        print(original)
