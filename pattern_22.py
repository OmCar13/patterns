n = 7 

for i in range(n):
    for j in range(n):

        distance_from_edge = min(i, j, n - 1 - i, n - 1 -j)
        
        print(n // 2 + 1 - distance_from_edge, end="")
    
    print()


