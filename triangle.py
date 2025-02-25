rows = 4

for i in range(rows):
    for j in range(rows -i):
        print(" ", end="")
    
    for j in range(i + 1):
        print("*", end=" ")    
    print()
