n = 11

for i in range(n):
    if i == n // 2:
        continue
    for j in range(abs(n // 2 - i)):
        print("*", end="")
    for j in range(2 * (n // 2 - (abs(n // 2 - i)))):
        print(" ", end="")
    for j in range(abs(n // 2 - i)):
        print("*", end="")
    
    print()