map = ["A", "B", "C", "D", "E"]

for i in range(4):
    for j in range(3 - i):
        print(" ", end="")
    for j in range(i + 1):
        print(map[j], end="")
    for j in range(i - 1, -1, -1):
        print(map[j], end="")
    print()

    
