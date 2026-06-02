n = 9

for i in range(n):
    for j in range(4 - abs(i - 4) + 1):
        print("*", end="")
    for j in range(2 * abs(5 - i - 1)):
        print(" ", end="")
    for j in range(4 - abs(i - 4) + 1):
        print("*", end="")
    print()