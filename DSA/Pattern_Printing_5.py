n = int(input("Enter no of rows : "))
num = 0 

for i in range(n, 0, -1):
    for j in range(i):
        # print(chr(65 + j), end=" ")
        print(chr(65 + num), end=" ")
        num += 1
    print()
