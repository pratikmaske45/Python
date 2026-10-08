# Printing a star pattern 
for i in range(1, 4):

    for j in range(1, 4 - i):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        print("*", end=" ")

    print()