# Ask the user to input a number for which they want to see the multiplication table

number = int(input ("Enter a number to see its multiplication table:"))

for x in range (1, 11):
    multiplication = number * x 
    print(f"{number} * {x} = {multiplication}")