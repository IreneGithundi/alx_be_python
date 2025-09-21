size = int(input("Enter the size of the pattern: "))
length = 1;

while length <= size:
    width = 1
    while width <= size:
        print("*", end="")
        width += 1
    print()
    length += 1