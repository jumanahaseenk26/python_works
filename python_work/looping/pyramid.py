for row in range(1,7):
    for space in range(7-row,1,-1):
        print(end=" ")
    for st in range(row):
        print("* ",end="")
    print()