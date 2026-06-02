for i in range(5):
    for j in range(i+1):
        if i % 2 == 0:
            print(1 - (j % 2), end="")
        else:
            print(j % 2, end="")
    print()