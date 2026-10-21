# n = int(input("enter no of rows : "))
n = 5
sp = 8
for i in range(1, n+1):
    for s in range(0, sp):
        print(end = " ")
    for j in range(1, i+1):
        print(j, end = " ")
    if (i != 1):
        print("1")
    print()
    sp -= 1

# n = 5
# for i in range(1, n + 1):
#     print("  " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
#     print()