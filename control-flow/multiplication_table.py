number = int(input("Enter a number to see its multiplication table:"))

for multiplier in range (1, 11):
    result = multiplier * number
    print(f"{number} * {multiplier} = {result}")