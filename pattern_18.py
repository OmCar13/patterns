map = ["A", "B", "C", "D", "E"]

for i in range(5):
    for j in range(i + 1):
        print(map[4 - i + j], end="")
    print()