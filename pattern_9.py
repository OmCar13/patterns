n = 9

for i in range(n):
    for j in range(abs(i - n // 2)):
        print(" ", end="")

    for j in range(n - 2 * abs(i - n // 2)):
        print("*", end="")

    if i == n // 2:
        print()
        print("*" * n, end="")

    print() 