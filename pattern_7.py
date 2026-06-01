for i in range(5):
    for j in range(5 - i - 1): # 5 - o - 1 = 4 i.e. 4 space in the first iteration and so on  
        print(" ", end="")
    for j in range(2 * i + 1): # 2 * 0 + 1 = 1 i.e. no. of stars and increasing it to odd number every iteration
        print("*", end="")
    print()

