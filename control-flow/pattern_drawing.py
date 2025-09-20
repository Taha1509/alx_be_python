
# prompt the user to enter a positive integer
number = int (input("Enter the size of the pattern:"))

row = 0
while row < number:
    for x in range (1 , number + 1):
        print ("#", end="")
    print ()
    row += 1