print("\nSTART\n")
numbers = [5, 2, 5, 2, 2]
# Print rows of X characters, where each row length is determined by the corresponding number in the array

for row_index in range(len(numbers)):
    for x_index in range(numbers[row_index]):
        print("X", end="")
    print()  # to move to the next line after each row

print("\nEND\n")