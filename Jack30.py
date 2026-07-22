num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

for i in range(1, max(num1, num2)):
    if num1 % i == num2 % i == 0:
        hcf = i

lcm = (num1*num2)//hcf

print("LCM =", lcm)
