map = ["A", "B", "C", "D", "E"]

for i in range(5):
    for j in range(i + 1):
        print(map[j], end="")
    print()