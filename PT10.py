A=int(input("Enter the starting number:"))
B=int(input("Enter the ending number:"))

for i in range(A,B+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
